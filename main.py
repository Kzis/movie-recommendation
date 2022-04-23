from fastapi import FastAPI
import setting
import uvicorn

from model_api import recommendations

app = FastAPI()
app.include_router(recommendations.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    setting.init_global_data()
    uvicorn.run(app, host="0.0.0.0", port=8000 , reload=True)