"""Verify a real requirement analysis foreign-key relation without storing brief text."""
import sqlite3
from app.features.requirements.providers.provider_record_requirement import provider_record_requirement

def test_requirement_request_analysis_fk(tmp_path):
    path = str(tmp_path / "requirements.sqlite3")
    identifier = provider_record_requirement("Confidential product brief", "Actors: admin", path)
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT brief_char_count FROM requirement_requests WHERE id=?", (identifier,)).fetchone()[0] == 26
        assert connection.execute("SELECT status FROM requirement_analyses WHERE requirement_id=?", (identifier,)).fetchone()[0] == "extracted"
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
    assert b"Confidential product brief" not in (tmp_path / "requirements.sqlite3").read_bytes()
