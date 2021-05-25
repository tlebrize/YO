from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
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


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    ...
