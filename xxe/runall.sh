#!/bin/bash
cd /app/wtv && nohup python3 -m http.server 5001 --bind 127.0.0.1 &
su flaskit -c '/home/flaskit/.local/bin/flask run --host 0.0.0.0'

