from fastapi import FastAPI
from .api import app as api_app
from .database import engine
from .models import Base

# Create the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(api_app, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Watch API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
