from fastapi import APIRouter, HTTPException
from models.command_model import CommandLog
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.post("/log")
def log_phrase(command: CommandLog):
    global cursor
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", ""),
            database=os.getenv("DB_NAME", "to_do_voz")
        )
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