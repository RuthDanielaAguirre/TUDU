from fastapi import APIRouter, HTTPException

from config.database import get_db_connection
from models.command_model import CommandLog
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/commands", tags=["Commands"])


@router.post("/log")
def log_phrase(command: CommandLog):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor= conn.cursor()

        sql = "INSERT INTO command_logs (phrase, action,type) VALUES (%s, %s, %s)"
        values = (command.phrase, command.action, command.type)

        cursor.execute(sql, values)
        conn.commit()
        return{"message": "The command was added"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()