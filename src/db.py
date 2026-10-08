"""SalonGo database layer (SQLite).

Tables, sample data, salon queries, slots, booking, accounts and owner tools.
Uses only Python's built-in sqlite3, so there is nothing extra to install.
"""
import os
import re
import secrets
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone

from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.environ.get("VERCEL"):
    # Vercel's disk is temporary: only /tmp is writable, and it resets often.
    DB_PATH = "/tmp/salongo.db"
else:
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)
    DB_PATH = os.path.join(BASE_DIR, "database", "salongo.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL DEFAULT 'customer'
                  CHECK (role IN ('customer', 'owner', 'admin')),
    is_active     INTEGER NOT NULL DEFAULT 1,
    created_at    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS salons (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id    INTEGER NOT NULL REFERENCES users(id),
    name        TEXT NOT NULL,
    address     TEXT,
    distance_km REAL NOT NULL DEFAULT 0,
    rating      REAL NOT NULL DEFAULT 0,
    emoji       TEXT NOT NULL DEFAULT 'ðŸ’ˆ',
    status      TEXT NOT NULL D¶»§q«^