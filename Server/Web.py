from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn

try:
    import uvloop
    uvloop.install()
except ImportError:
    uvloop = None

from Utils.Config import settings
from Server.Accounts.Create import create_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#@app.on_event("startup")
#async def services_preflight():


def start(args):
    app.include_router(create_router)
    uvicorn.run(app, host=settings.host, port=settings.port)
