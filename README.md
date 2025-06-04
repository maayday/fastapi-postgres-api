# FastAPI + PostgreSQL API

This is a REST API built with FastAPI, connected to a local PostgreSQL database, supporting:

- Item creation (POST /items/)
- Item retrieval with filters and pagination (GET /items/)
- SQLAlchemy integration
- PostgreSQL database at port 5433

## Setup

1. Clone the repo
2. Create a `.env` file:

DATABASE_URL=postgresql://postgres:poij@localhost:5433/ecommerce_analytics


3. Install dependencies:
pip install -r requirements.txt


4. Run the app:
uvicorn main:app --reload