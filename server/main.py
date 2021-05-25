from fastapi import FastAPI
from .routers import episode, attribute
from .settings import HOST

app = FastAPI()

app.include_router(episode)
app.include_router(attribute)


@app.get("/")
def root():
    return {
        "search": f"{HOST}/episode/search/?query=yoga",
        "by attributes": f"{HOST}/attribute/",
    }
