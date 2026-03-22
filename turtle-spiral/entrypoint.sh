#!/bin/bash
# xvfb-run starts a temporary virtual framebuffer and sets DISPLAY automatically.
# -a = auto-select display number (avoids conflicts if multiple are running)
echo "Starting virtual framebuffer and drawing spiral..."
xvfb-run -a python3 spiral.py
