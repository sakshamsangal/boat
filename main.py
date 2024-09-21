import uvicorn
from fastapi import FastAPI
from controller import submit_api, db


app = FastAPI()

app.include_router(submit_api.app)
app.include_router(db.app)


if __name__ == "__main__":
    # uvicorn main:app --reload --port 5000
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=False)
