#!/usr/bin/bash

flask --app backend.py run --port=5001 &
flask --app backend.py run --port=5002 &
flask --app backend.py run --port=5003 &
flask --app backend.py run --port=5004 &

flask --app load_balancer.py run --port=7000 --host=0.0.0.0 & 
