#!/bin/sh
source ~/iKibble/venv/bin/activate
python3 ~/iKibble/ikibble/web_app.py &
chromium-browser -kiosk 127.0.0.1:5000