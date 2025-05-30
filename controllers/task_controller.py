from fastapi import APIRouter, HTTPException, Path, Body
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


@router.delete("/delete-by-description")
def delete_task_by_description(description: str = Body(...), id_user: int = Body(...)):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        DELETE FROM tasks 
        WHERE description = %s AND id_user = %s
        """
        cursor.execute(sql, (description, id_user))
        conn.commit()

        if cursor.rowcount > 0:
            return {"message": "Tarea eliminada correctamente"}
        else:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@router.put("/update-by-description")
def update_task_by_description(
    old_description: str = Body(...),
    new_description: str = Body(...),
    id_user: int = Body(...)
):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE tasks
        SET description = %s
        WHERE description = %s AND id_user = %s
        """
        values = (new_description, old_description, id_user)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            return {"message": "Task updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Task not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@router.put("/update/{task_id}")
def update_task(task_id: int, new_description: str = Body(...)):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "UPDATE tasks SET description = %s WHERE id_task = %s"
        cursor.execute(sql, (new_description, task_id))
        conn.commit()

        if cursor.rowcount > 0:
            return {"message": "Task updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Task not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
