# Run multiple Docker containers
docker run -d -p 5001:5000 --name object_storage_2 object_storage:latest
docker run -d -p 5002:5000 --name object_storage_3 object_storage:latest

