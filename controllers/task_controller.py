from fastapi import APIRouter, HTTPException
from config.database import get_db_connection
from models.task_model import TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/tasks/create")

def create_task(task: TaskCreate):
    conn= None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()


        sql = """
        INSERT INTO tasks (description, created_date, state, id_user, id_type_task, id_tag_task, repeat_interval)
        VALUES (%s, CURDATE(), 1, %s, %s, %s, %s)
        """
        values = (
            task.description,
            task.id_user,
            task.id_type_task,
            task.id_tag_task,
            task.repeat_interval
        )

        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Tarea creada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
