# Build the Docker image
docker build -t object_storage:latest .

# Run the Docker container
docker run -d -p 5000:5000 --name object_storage_1 object_storage:latest

