#!/bin/bash

# Define the base URL
BASE_URL="http://localhost:5002"

# Store a key-value pair
echo "Storing key-value pair..."
curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "1", "value": "uno"}'

curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "2", "value": "due"}'

curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "3", "value": "tre"}'

echo -e "\n"

# Retrieve the value by key
echo "Retrieving value for key 'myKey'..."
curl -X GET $BASE_URL/retrieve/2
curl -X GET $BASE_URL/retrieve/4

echo -e "\n"

