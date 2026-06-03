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
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute(
        "SELECT * FROM posts WHERE id = ?",
        (post_id,)
    ).fetchone()
    connection.close()
    return post
def create_post(title, body):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO posts (title, body) VALUES (?, ?)",
        (title, body)
    )
    connection.commit()
    connection.close()

def update_post(post_id, title, body):
    connection = get_db_connection()
    connection.execute(
        "UPDATE posts SET title = ?, body = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (title, body, post_id)
    )
    connection.commit()
    connection.close()

def delete_post(post_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM posts WHERE id = ?",
        (post_id,)
    )

    connection.commit()
    connection.close()

def get_comments_for_post(post_id):
    connection = get_db_connection()
    comments = connection.execute(
        "SELECT * FROM comments WHERE post_id = ? ORDER BY created_at DESC",
        (post_id,)
    ).fetchall()
    connection.close()
    return comments 

def create_comment(post_id, title, body):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO comments (post_id, title, body) VALUES (?, ?, ?)",
        (post_id, title, body)
    )
    connection.commit()
    connection.close()