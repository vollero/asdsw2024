# Build the Docker image
docker build -t consistent_hashing_lb:latest .

# Run the Docker container
docker run -d -p 80:80 --name consistent_hashing_lb --link object_storage_1 --link object_storage_2 --link object_storage_3 consistent_hashing_lb:latest

