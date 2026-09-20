import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "ai_life_agent.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            main_goal TEXT,
            focus_area TEXT,
            daily_available_minutes INTEGER,
            onboarding_completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def create_or_update_user(
    telegram_id: int,
    username: str | None,
    first_name: str | None,
    last_name: str | None,
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (
            telegram_id,
            username,
            first_name,
            last_name
        )
        VALUES (?, ?, ?, ?)
        ON CONFLICT(telegram_id)
        DO UPDATE SET
            username = excluded.username,
            first_name = excluded.first_name,
            last_name = excluded.last_name
    """, (
        telegram_id,
        username,
        first_name,
        last_name,
    ))

    connection.commit()
    connection.close()


def update_onboarding(
    telegram_id: int,
    main_goal: str,
    focus_area: str,
    daily_available_minutes: int,
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET
            main_goal = ?,
            focus_area = ?,
            daily_available_minutes = ?,
            onboarding_completed = 1
        WHERE telegram_id = ?
    """, (
        main_goal,
        focus_area,
        daily_available_minutes,
        telegram_id,
    ))

    connection.commit()
    connection.close()