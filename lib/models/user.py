from db.database import create_conn

class User:
    @classmethod
    def create_table(cls, cursor):
        sql = """ 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
        cursor.execute(sql)

    @classmethod
    def create(cls, name, email):
        with create_conn() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO users (name, email) VALUES (?, ?)"
            cursor.execute(sql, (name, email))
            conn.commit()
            return cls.find_by_id(cursor.lastrowid)

    @classmethod
    def delete(cls, user_id):
        with create_conn as conn:
            cursor = conn.cursor()
            sql = "DELETE FROM users WHERE id = ?"
            cursor.execute(sql, (user_id))
            conn.commit()
            return cursor.rowcount > 0
        
            