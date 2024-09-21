from fastapi import APIRouter, Request
from starlette.responses import StreamingResponse

import controller.db_con as db_con
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = APIRouter()
templates = Jinja2Templates(directory="templates")


async def slow_numbers(users, ls):
    s = '<table class="table table-sm table-bordered"><tr>'
    for item1 in ls:
        s = s + '<th>' + item1 + '</th>'
    yield s + '</tr>'

    for user in users:
        s = '<tr>'
        for item in user:
            s = s + '<td>' + str(item) + '</td>'
        yield s + '</tr>'
    yield '</table>'


#
# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="home.html"
#     )

@app.get("/users/{tb}", response_class=StreamingResponse)
async def read_users(tb: str):
    print(tb)
    cursor = db_con.connection.cursor()
    query = f"SELECT * FROM {tb} limit 100"
    cursor.execute(query)
    users = cursor.fetchall()

    x = cursor.execute(f"SHOW columns FROM {tb}")
    cursor.execute(x)
    ls = []
    for column in cursor.fetchall():
        ls.append(column[0])

    s = slow_numbers(users, ls)
    return StreamingResponse(s, media_type='text/html')
    # return templates.TemplateResponse('temp.html', context={'request': request, 'result': users})


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )


@app.get("/pl", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="pl.html"
    )
