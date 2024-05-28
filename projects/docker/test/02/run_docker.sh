# Build the Docker image
docker build -t nginx_load_balancer:latest .

# Run the Docker container
docker run -d -p 80:80 --name load_balancer --link object_storage_1 --link object_storage_2 --link object_storage_3 nginx_load_balancer:latest

