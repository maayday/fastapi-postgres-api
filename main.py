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

from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = updated_item.name
    item.price = updated_item.price
    item.in_stock = updated_item.in_stock

    db.commit()
    db.refresh(item)
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"detail": f"Item with id {item_id} deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
