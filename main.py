from fastapi import FastAPI
from app.dependencies.database import engine, Base
from app.api.v1 import todo

# Create the FastAPI app instance
app = FastAPI()

# Include API routers
app.include_router(todo.router, prefix="/api/v1", tags=["todos"])


# Create the database tables
def create_db_tables():
    Base.metadata.create_all(bind=engine)


# Call the function to create tables
create_db_tables()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

