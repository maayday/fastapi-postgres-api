from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# -----------------------
# Dependency to get DB
# -----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------
# Pydantic input model
# -----------------------
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# -----------------------
# POST endpoint
# -----------------------
@app.post("/items/")
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = models.Item(
        name=item.name,
        price=item.price,
        in_stock=item.in_stock
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

from typing import Optional
from fastapi import Query

@app.get("/items/")
def read_items(
    in_stock: Optional[bool] = Query(None),
    min_price: Optional[float] = Query(None),
    name: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(models.Item)

    if in_stock is not None:
        query = query.filter(models.Item.in_stock == in_stock)

    if min_price is not None:
        query = query.filter(models.Item.price >= min_price)

    if name:
        query = query.filter(models.Item.name.ilike(f"%{name}%"))

    items = query.offset(skip).limit(limit).all()
    return items
