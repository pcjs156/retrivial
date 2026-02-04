from fastapi import FastAPI
import uvicorn

from src.jsonplaceholder import jsonplaceholder_router

app = FastAPI(title="Retrivial", description="A simple API for retrieving data")

app.include_router(jsonplaceholder_router)

@app.get("/")
def read_root():
    return {"message": "Hello from retrivial!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
