import os
import sys

SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Import the application from src explicitly. `from app import app` resolves
# to this root-level entrypoint on Vercel and can import the module recursively.
from src.app import app
