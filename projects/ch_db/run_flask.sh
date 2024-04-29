#!/usr/bin/bash

flask --app $1 run --port=$2 --host=0.0.0.0
