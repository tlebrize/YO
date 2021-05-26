from fastapi import FastAPI
from .routers import episode, attribute, auth
from .settings import Settings

app = FastAPI()

app.include_router(episode)
app.include_router(attribute)
app.include_router(auth)


@app.get("/")
def root():
    return {
        "search": f"{Settings.HOST}/episode/search/?query=yoga",
        "by attributes": f"{Settings.HOST}/attribute/",
    }
