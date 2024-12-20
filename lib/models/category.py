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
    
        