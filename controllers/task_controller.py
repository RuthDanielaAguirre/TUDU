from fastapi import APIRouter, HTTPException, Path
from config.database import get_db_connection
from models.task_model import TaskCreate


router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create")

def create_task(task: TaskCreate):
    conn = None
    cursor = None
    try:
        print("Datos recibidos:")
        print("description:", task.description)
        print("id_user:", task.id_user)
        print("id_type_task:", task.id_type_task)
        print("id_tag_task:", task.id_tag_task)
        print("repeat_interval:", task.repeat_interval)

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

        print("Ejecutando SQL con:")
        print("SQL:", sql)
        print("VALUES:", values)

        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Tarea creada correctamente"}

    except Exception as e:
        print("ERROR AL INSERTAR:", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@router.get("/by-user/{id_user}")
def get_tasks_by_user(id_user: int = Path(..., description="ID del usuario")):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
        SELECT 
            t.id_task,
            t.description,
            t.state,
            t.created_date,
            t.repeat_interval,
            tt.name AS type_name  
        FROM tasks t
        LEFT JOIN types_tasks tt ON t.id_type_task = tt.id_type_task
        WHERE t.id_user = %s
        ORDER BY t.created_date DESC
        """
        cursor.execute(sql, (id_user,))
        tasks = cursor.fetchall()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor: cursor.close()
        if conn: conn.close()