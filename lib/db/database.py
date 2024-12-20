import sqlite3

def create_conn():
    return sqlite3.connect("inventory.db")