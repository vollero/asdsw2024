curl -X POST http://localhost/store -H "Content-Type: application/json" -d '{"key": "myKey", "value": "myValue"}'

curl -X GET http://localhost/retrieve/myKey
