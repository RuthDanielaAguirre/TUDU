from fastapi import FastAPI
#from controllers.user_controller import router as user_router
from controllers.voice_controller import router as voice_router
from controllers.command_controller import router as command_router
from controllers.task_controller import router as task_router
from controllers.subtask_controller import router as subtask_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="TUDU",
    description="Backend de la aplicación de gestión de tareas con comandos por voz",
    version="1.0.0"
)

@app.get('/')
def root():
    return{"message": "Welcome to TUDU"}

app.include_router(voice_router)
app.include_router(command_router)
app.include_router(task_router)
app.include_router(subtask_router)

for route in app.routes:
    print(f"✅ {route.path} [{route.name}]")

