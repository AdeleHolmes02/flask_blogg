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
def create_post(title, body, tags_text=""):
    connection = get_db_connection()

    cursor = connection.execute(
        "INSERT INTO posts (title, body) VALUES (?, ?)",
        (title, body)
    )

    post_id = cursor.lastrowid

    connection.commit()
    connection.close()

    if tags_text:
        tags = [tag.strip() for tag in tags_text.split(",")]

        for tag_name in tags:
            if tag_name:
                tag_id = get_or_create_tag(tag_name)
                add_tag_to_post(post_id, tag_id)

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

def get_or_create_tag(name):
    connection = get_db_connection()

    tag = connection.execute(
        "SELECT * FROM tags WHERE name = ?",
        (name,)
    ).fetchone()

    if tag:
        connection.close()
        return tag["id"]

    cursor = connection.execute(
        "INSERT INTO tags (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    tag_id = cursor.lastrowid
    connection.close()

    return tag_id


def add_tag_to_post(post_id, tag_id):
    connection = get_db_connection()
    connection.execute(
        "INSERT OR IGNORE INTO post_tags (post_id, tag_id) VALUES (?, ?)",
        (post_id, tag_id)
    )
    connection.commit()
    connection.close()

def get_tags_for_post(post_id):
    connection = get_db_connection()
    tags = connection.execute(
        """
        SELECT tags.*
        FROM tags
        JOIN post_tags ON tags.id = post_tags.tag_id
        WHERE post_tags.post_id = ?
        ORDER BY tags.name
        """,
        (post_id,)
    ).fetchall()
    connection.close()
    return tags