from fastapi import FastAPI
from controllers.user_controller import router as user_router
from controllers.task_controller import router as task_router
from controllers.voice_controller import router as voice_router


app = FastAPI()

@app.get('/')
def root():
    return{"message": "Welcome to TUDU"}



app.include_router(voice_router, prefix="/voice", tags=["Voice"])
