import sqlite3

DATABASE = "blog.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def get_all_posts():
    connection = get_db_connection()
    posts = connection.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()
    connection.close()
    return posts