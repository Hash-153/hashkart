"""
NovaMart Platform Top-Level Launcher
====================================
Launches the full-stack NovaMart e-commerce application (FastAPI backend + Vite frontend).
"""

import os
import subprocess
import sys
import time

def start_backend():
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    return subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
        cwd=backend_dir,
    )

def main():
    print("=" * 60)
    print("  Starting NovaMart E-Commerce Platform")
    print("  Backend API:  http://localhost:8000/docs")
    print("  Storefront:   http://localhost:5173/")
    print("=" * 60)
    proc = start_backend()
    try:
        proc.wait()
    except KeyboardInterrupt:
        print("\nStopping NovaMart platform...")
        proc.terminate()

if __name__ == "__main__":
    main()
