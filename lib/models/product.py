from db.database import create_conn

class Product:
    @classmethod
    def create_table(cls, cursor):
        sql = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
        """
        cursor.execute(sql)
    
    @classmethod
    def create(cls, name, price, category_id):
        with create_conn() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)"
            cursor.execute(sql, (name, price, category_id))
            conn.commit()
            product_id = cursor.lastrowid
        return cls.find_by_id(product_id)    