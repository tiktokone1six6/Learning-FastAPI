from fastapi import FastAPI
from .database import engine, Base
from .routes import jokes, users, login


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jokes.router)
app.include_router(users.router)
app.include_router(login.router)

@app.get("/")
def root():
    return {"message": "FastAPI CRUD app running!"}
