#!/usr/bin/bash

cd db1
flask --app simple_db.py run --port=6000 --host=0.0.0.0 &
cd ..

cd db2
flask --app simple_db.py run --port=6001 --host=0.0.0.0 &
cd ..

cd db3
flask --app simple_db.py run --port=6002 --host=0.0.0.0 &
cd ..
