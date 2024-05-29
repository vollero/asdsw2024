#!/bin/bash
set -e

# Wait for InfluxDB to start
sleep 10

influx -execute "CREATE DATABASE weather"
influx -execute "CREATE USER admin WITH PASSWORD 'admin' WITH ALL PRIVILEGES"
influx -execute "GRANT ALL ON weather TO admin"

