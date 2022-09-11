import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)

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