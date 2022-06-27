#!/bin/sh
source ~/iKibble/venv/bin/activate
python3 ~/iKibble/web_app/web_app.py &
chromium-browser -kiosk 127.0.0.1:5000