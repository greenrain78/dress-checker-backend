import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from env import DB_URL
app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

@app.get("/hello")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })

@app.get("/")
async def main():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)