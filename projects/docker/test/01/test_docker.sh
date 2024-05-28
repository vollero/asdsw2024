#!/bin/bash

# Define the base URL
BASE_URL="http://localhost:5000"

# Store a key-value pair
echo "Storing key-value pair..."
curl -X POST $BASE_URL/store \
     -H "Content-Type: application/json" \
     -d '{"key": "myKey", "value": "myValue"}'

echo -e "\n"

# Retrieve the value by key
echo "Retrieving value for key 'myKey'..."
curl -X GET $BASE_URL/retrieve/myKey

echo -e "\n"

