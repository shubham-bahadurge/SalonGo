import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Import the Flask application explicitly from src. Importing `app` by its
# short name here can resolve back to this root entrypoint and recurse.
from src.app import app

# src/app.py lives one directory below the repository root, while Vercel's
# static assets are stored in the root-level public/ directory.
app.static_folder = os.path.join(ROOT_DIR, "public")
