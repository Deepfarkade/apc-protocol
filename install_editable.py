#!/usr/bin/env python
"""
Script to automate editable install of apc-core for development and usage.
Usage:
    python install_editable.py
"""
import subprocess
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
apc_core_path = os.path.join(project_root, 'apc_core')

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', apc_core_path])
    print("\n[APC] apc-core installed in editable mode! You can now import 'apc_core' from anywhere in this environment.")
except subprocess.CalledProcessError as e:
    print("[APC] Editable install failed:", e)
    sys.exit(1)
