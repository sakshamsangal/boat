import json
from typing import Annotated

from fastapi import Response, Query
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from starlette.responses import FileResponse, JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = APIRouter()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/pdf", response_class=FileResponse)
async def main():
    return "./static/temp.pdf"


class Item(BaseModel):
    response_type: str
    client_id: str
    scope: str
    state: str
    redirect_uri: str
    # nonce: str


@app.get("/authorize")
async def redirect_typer(item: Annotated[Item, Query()]):
    return RedirectResponse(
        f"http://127.0.0.1:8080/login/oauth2/code/boat?code=+WYT3XemV4f81ghHi4V+RyNwvATDaD4FIj0BpfFC4Wzg=&state={item.state}")


#
# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="home.html"
#     )

@app.post("/token")
def read_root():
    with open("./static/token.json") as foo:
        return Response(content=foo.read(), media_type='application/json')


@app.get("/jwk")
def read_root():
    with open("./static/jwk.json") as foo:
        return Response(content=foo.read(), media_type='application/json')


@app.get("/user")
def read_root():
    with open("./static/user.json") as foo:
        return Response(content=foo.read(), media_type='application/json')


@app.get("/.well-known/openid-configuration")
def read_root():
    with open("./static/auth.json") as foo:
        # json_str = json.dumps(foo, indent=4, default=str)
        return Response(content=foo.read(), media_type='application/json')
        # return Response(content=data, media_type="application/json")


@app.get("/xml")
def read_root1():
    with open("./static/temp.xml") as foo:
        data = foo.read()
        headers = {'Content-Disposition': 'inline; filename="out.xml"'}
        return Response(data, headers=headers, media_type='application/xml')

# import asyncio
#
#
# async def slow_numbers(minimum, maximum):
#     yield '<html><body><ul>'
#     for number in range(minimum, maximum + 1):
#         yield '<li>%d</li>' % number
#         await asyncio.sleep(0.5)
#     yield '</ul></body></html>'
#
#
# @app.get("/sr", response_class=StreamingResponse)
# async def app1():
#     generator = slow_numbers(1, 10)
#     return StreamingResponse(generator, media_type='text/html')
