"""SalonGo extras: admin, salon approval, reviews, service editing,
real-location support and login rate limiting. Builds on db.py."""
import os
import sqlite3
import time

from werkzeug.security import generate_password_hash

import db
from db import ACTIVE, get_db, now_ist

CATEGORY_CHOICES = ["haircut", "beard", "hair styling", "facial", "massage", "coloring", "other"]

# Sample salons are placed around Pune so "real distance" can be demonstrated.
SAMPLE_COORDS = {
    "Style Studio": (18.5314, 73.8446), "Royal Cuts": (18.5167, 73.8563),
    "Glow Beauty Lounge": (18.5362, 73.8939), "The Trim Box": (18.5196, 73.8553),
    "Zen Spa & Salon": (18.5074, 73.8077), "Color Theory": (18.5590, 73.7868),
}

LOGIN_WINDOW = 15 * 60
MAX_FAILS_PER_EMAIL = 5
MAX_FAILS_PER_IP = 20


def init_extras():
    conn = get_db()
    try:
        cols = [r["name"] for r in conn.execute("PRAGMA table_info(salons)")]
        for col in ("lat", "lng"):
            if col not in cols:
                conn.execute(f"ALTER TABLE salons ADD COLUMN {col} REAL")
        conn.execute("CREATE TABLE IF NOT EXISTS login_attempts ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL NOT NULL, "
                     "ip TEXT, email TEXT)")
        for name, (lat, lng) in SAMPLE_COORDS.items():
            conn.execute(
                "UPDATE salons SET lat = ?, lng = ? WHERE name = ? AND lat IS NULL AND owner_id = "
                "(SELECT id FROM users WHERE email = 'owner@salongo.local')", ¶»§q«^