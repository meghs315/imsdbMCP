import sqlite3

DB_PATH = "movies.db"


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scenes (
            movie_title TEXT,
            scene_number INTEGER,
            scene_summary TEXT,
            scene_text TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_scene(movie_title, scene_number, scene_summary, scene_text, cursor):
    cursor.execute("""
        INSERT INTO scenes (movie_title, scene_number, scene_summary, scene_text)
        VALUES (?, ?, ?, ?)
    """, (movie_title, scene_number, scene_summary, scene_text))

def insert_scenes(movie_title, scenes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for scene in scenes:
        insert_scene(
            movie_title,
            scene["scene_number"],
            scene["scene_summary"],
            scene["scene_text"],
            cursor
        )
    conn.commit()
    conn.close()