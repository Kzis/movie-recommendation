from fastapi import FastAPI
import setting
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    setting.init_global_data()
    uvicorn.run(app, host="0.0.0.0", port=8000 , reload=True)