from Server.Web import templates
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse

create_router = APIRouter(prefix="/Account")


@create_router.get("/Create", response_class=HTMLResponse)
async def create_user(request: Request):

    return templates.TemplateResponse("account/create.html", {"request": request})
