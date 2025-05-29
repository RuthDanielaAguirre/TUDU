from config.database import get_db_connection
import mysql.connector


def execute_sql_script(cursor, script):
    commands = script.strip().split(';')
    for command in commands:
        if command.strip():
            try:
                cursor.execute(command)
            except mysql.connector.Error as err:
                print(f"Error en comando:\n{command}\n{err}\n")

def setup_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        print("Iniciando configuración de la base de datos...")

        # Eliminación de tablas
        execute_sql_script(cursor, """
            DROP TABLE IF EXISTS 
                phrases,
                commands,
                command_logs,
                tasks,
                tags_tasks,
                types_tasks,
                users,
                profiles;
        """)

        #  Creación de tablas
        execute_sql_script(cursor, """
            CREATE TABLE profiles (
                id_profile INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(10) NOT NULL
            );

            CREATE TABLE users (
                id_user INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(20) NOT NULL,
                password VARCHAR(15) NOT NULL,
                email VARCHAR(50) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                id_profile INT,
                FOREIGN KEY (id_profile) REFERENCES profiles(id_profile)
            );

            CREATE TABLE types_tasks (
                id_type_task INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(25) NOT NULL
            );

            CREATE TABLE tags_tasks (
                id_tag_task INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50),
                difficulty VARCHAR(15),
                importancy VARCHAR(15),
                color VARCHAR(10)
            );

            CREATE TABLE tasks (
                id_task INT PRIMARY KEY AUTO_INCREMENT,
                description VARCHAR(255) NOT NULL,
                created_date DATE,
                due_date DATE,
                closed_date DATE,
                state INT,
                id_user INT,
                id_type_task INT,
                id_tag_task INT,
                FOREIGN KEY (id_user) REFERENCES users(id_user),
                FOREIGN KEY (id_type_task) REFERENCES types_tasks(id_type_task),
                FOREIGN KEY (id_tag_task) REFERENCES tags_tasks(id_tag_task)
            );

            CREATE TABLE commands (
                id_command INT PRIMARY KEY AUTO_INCREMENT,
                command VARCHAR(255) NOT NULL
            );

            CREATE TABLE phrases (
                id_phrase INT PRIMARY KEY AUTO_INCREMENT,
                phrase VARCHAR(255) NOT NULL,
                id_command INT,
                FOREIGN KEY (id_command) REFERENCES commands(id_command)
            );

            CREATE TABLE command_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                phrase TEXT NOT NULL,
                action VARCHAR(50),
                type VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Inserciones iniciales
        cursor.execute("INSERT IGNORE INTO profiles (name) VALUES ('estudiante'), ('trabajo'), ('ambos'), ('admin');")
        cursor.execute("INSERT IGNORE INTO tags_tasks (name, difficulty, importancy, color) VALUES ('Default', 'Medium', 'Normal', '#AAAAAA');")
        cursor.execute("INSERT IGNORE INTO types_tasks (name) VALUES ('Simple'), ('Subtask'), ('Recurring');")
        cursor.execute("INSERT IGNORE INTO users (username, password, email, gender, id_profile) VALUES ('daniela', '1234', 'daniela@example.com', 'female', 2);")

        conn.commit()
        print(" Base de datos configurada correctamente.")

    except mysql.connector.Error as e:
        print(f"Error al configurar la base de datos: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

if __name__ == "__main__":
    setup_database()
