from fastapi import FastAPI
from controllers.voice_controller import router as voice_router


app = FastAPI()

@app.get('/')
def root():
    return{"hello": "world"}

app.include_router(voice_router)
