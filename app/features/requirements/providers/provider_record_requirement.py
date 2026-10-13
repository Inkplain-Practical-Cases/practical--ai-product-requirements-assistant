"""SQLite repository for minimal, non-sensitive product requirement analysis metadata."""
import os
import sqlite3
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone

def provider_record_requirement(brief: str, analysis: str, db_path: str | None = None) -> str:
    """Save request/analysis lengths and state, never the original requirement text."""
    path = db_path or os.getenv("INKPLAIN_REQUIREMENTS_DB", "data/requirements.sqlite3")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    rid = uuid4().hex
    at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS requirement_requests (
            id TEXT PRIMARY KEY,
            brief_char_count INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS requirement_analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requirement_id TEXT NOT NULL REFERENCES requirement_requests(id),
            result_char_count INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        connection.execute("INSERT INTO requirement_requests(id, brief_char_count, created_at) VALUES (?, ?, ?)",
                           (rid, len(brief), at))
        connection.execute("INSERT INTO requirement_analyses(requirement_id, result_char_count, status, created_at) VALUES (?, ?, ?, ?)",
                           (rid, len(analysis), "extracted", at))
    return rid
