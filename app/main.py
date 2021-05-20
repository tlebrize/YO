from fastapi import FastAPI
from .routers import episode, attribute

app = FastAPI()

app.include_router(episode)
app.include_router(attribute)
