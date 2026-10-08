import os
import secrets

from flask import (Flask, abort, g, jsonify, redirect, render_template, request,
                   session)

import db
import extras

# "public" is where Vercel serves static files from.
app = Flask(__name__, static_folder="public", static_url_path="")

app.config.update(
    # On Vercel set SECRET_KEY in the project settings so logins survive restarts.
    SECRET_KEY=os.environ.get("SECRET_KEY") or (
        secrets.token_hex(32) if os.environ.get("VERCEL") else "dev-only-secret-change-me"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=bool(os.environ.get("VERCEL")),
)

CATEGORIES = [
    ("Haircut", "✂️"), ("Beard", "🧔"), ("Hair Styling", "💇"), ("Facial", "🧖"),
    ("Massage", "💆"), ("Coloring", "🎨"), ("Other", "✨"),
]
LOCATIONS = ["Central Market", "Riverside", "Old Town", "Tech Park"]
STATUS_LABELS = {"available": "Available", "busy": "Busy", "closed": "Closed",
                 "full": "Fully booked"}

# Create the tables (and sample salons the first time) when the app starts.
db.init_db()
extras.init_extras()


# ----------------------------- helpers -------------------------------------
def current_user():
    if "user" not in g:
        uid = session.get("user_id")
        g.user = db.get_user(uid) if uid else None
        if uid and g.user is None:
            session.pop("user_id", None)
    return g.user


def csrf_token():
    if "csrf" not in session:
        session���q�^