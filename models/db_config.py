from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        auth_plugin='mysql_native_password',
    )

if __name__ == "__main__":
    try:
        connection = get_connection()
        print("✅ Conexión exitosa a la base de datos.")
        connection.close()
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")