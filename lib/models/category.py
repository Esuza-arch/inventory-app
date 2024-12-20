from db.database import create_conn

class Category:
    @classmethod
    def create_table(cls, cursor):
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        cursor.execute(sql)

    @classmethod
    def create(cls, name):
        with create_conn() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO categories (name) VALUES (?)"
            cursor.execute(sql, (name,))
            conn.commit()
            category_id = cursor.lastrowid
        return cls.find_by_id(category_id)    
    
    @classmethod
    def delete(cls, category_id):
        with create_conn() as conn:
            cursor = conn.cursor()
            sql = "DELETE FROM categories WHERE id = ?"
            cursor.execute(sql, (category_id,))
            conn.commit()
            return cursor.rowcount > 0