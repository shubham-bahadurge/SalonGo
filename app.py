import os
import sys
import runpy

from flask import Flask

# Make the existing SalonGo source modules importable.
SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Explicit top-level Flask instance for Vercel's Flask detector.
app = Flask(__name__)

# Load the existing application without changing its routes or database logic.
_loaded = runpy.run_path(
    os.path.join(SRC_DIR, "app.py"),
    run_name="salongo_app",
)
app = _loaded["app"]
