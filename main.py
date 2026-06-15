from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "hello world"}


from fastapi.responses import FileResponse

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)