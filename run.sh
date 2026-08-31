#!/usr/bin/env bash
#git pull
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# Repo root on PYTHONPATH provides both the flow_mpc source and the local
# pure-Python `sdf_tools` shim (replacing the ROS/C++ package). The project venv
# (.venv, created with --system-site-packages) supplies colorednoise / gpytorch /
# nflows on top of the system torch / cv2 / numpy, so no sudo install is needed.
PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH" "$SCRIPT_DIR/.venv/bin/python" "$SCRIPT_DIR/scripts/test_control.py" --config mppi.yaml
