## 📄 `README.md`


# FastAPI + PostgreSQL API

This is a production-ready REST API built with **FastAPI** and **PostgreSQL**, designed for managing inventory-style items. The app supports creating, reading, filtering, and paginating items stored in a relational database.

## 🚀 Features

- ✅ Create items with name, price, and stock status
- ✅ Retrieve all items with optional filters:
  - `?in_stock=true`
  - `?min_price=50`
  - `?name=desk`
- ✅ Pagination support using:
  - `?skip=0&limit=10`
- ✅ SQLAlchemy ORM models
- ✅ PostgreSQL database with environment-secure credentials
- ✅ Fully documented Swagger UI at `/docs`

## 🎬 Swagger UI Demo

![Swagger UI Demo](https://github.com/user-attachments/assets/f17d52ed-9e8e-4547-870c-82604d29ca55)

## 📄 Example Responses

### POST /items/
**Request:**
json
{
  "name": "Standing Desk",
  "price": 299.99,
  "in_stock": true
}
**Response:**
{
  "id": 1,
  "name": "Standing Desk",
  "price": 299.99,
  "in_stock": true
}
### GET /items/?in_stock=true&min_price=200
**Response:**
json
[
  {
    "id": 1,
    "name": "Standing Desk",
    "price": 299.99,
    "in_stock": true
  }
]



## 🧱 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL 16 (Local)](https://www.postgresql.org/)
- [pgAdmin 4](https://www.pgadmin.org/)
- [Uvicorn](https://www.uvicorn.org/) for async server

## 🗂️ Project Structure



fastapi\_project/
│
├── database.py        # DB connection and session management
├── models.py          # SQLAlchemy table schema
├── main.py            # FastAPI routes and logic
├── requirements.txt   # Python dependencies
├── .env               # DB connection string (excluded from Git)
├── .gitignore         # Excludes .env, **pycache**, etc.
└── README.md


## ⚙️ Setup Instructions

### 1. Clone the repo

bash
git clone https://github.com/yourusername/fastapi-postgres-api.git
cd fastapi-postgres-api


### 2. Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows


### 3. Install dependencies

bash
pip install -r requirements.txt


### 4. Create a `.env` file

env
DATABASE_URL=postgresql://postgres:<your_password>@localhost:5433/ecommerce_analytics


> Replace `<your_password>` with your actual PostgreSQL password.

### 5. Run the app

bash
uvicorn main:app --reload --port 8001


### 6. Explore the API

* Interactive docs: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

---

## 🙌 Author

Built by Mehdi Hindi — data engineer in training, passionate about APIs and data systems.


