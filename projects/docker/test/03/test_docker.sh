#!/bin/bash

# Define the base URL
BASE_URL="http://localhost"

# Store a key-value pair
echo "Storing key-value pair..."
curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "10", "value": "dieci"}'

curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "11", "value": "undici"}'

curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "12", "value": "dodici"}'

curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "13", "value": "tredici"}'

echo -e "\n"

# Retrieve the value by key
echo "Retrieving value for key ''..."
curl -X GET $BASE_URL/retrieve/10
curl -X GET $BASE_URL/retrieve/11
curl -X GET $BASE_URL/retrieve/12
curl -X GET $BASE_URL/retrieve/13

echo -e "\n"

# Verify round-robin behavior (you may need to run this multiple times)
#for i in {1..3}; do
#    echo "Retrieving value for key '1' (Round $i)..."
#    curl -X GET $BASE_URL/retrieve/1
#    echo -e "\n"
#done

