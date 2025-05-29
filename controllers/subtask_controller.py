from fastapi import APIRouter, HTTPException
from config.database import get_db_connection
from models.subtask_model import SubtaskCreate

router = APIRouter(prefix="/subtasks", tags=["Subtasks"])

@router.post("/create")
def create_subtask(subtask: SubtaskCreate):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO subtasks (description, created_date, due_date, state, id_task_parent)
        VALUES (%s, CURDATE(), %s, %s, %s)
        """
        values = (
            subtask.description,
            subtask.due_date,
            subtask.state,
            subtask.id_task_parent
        )

        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Subtarea creada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
