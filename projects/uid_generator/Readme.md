# TEST UUID GENERATOR WITH

    curl http://localhost:6000/generate/uuid

# TEST INCREMENTAL ID WITH

    curl http://localhost:6000/generate/incremental

# TEST SHORT ID WITH

    curl http://localhost:6000/generate/short?length=8

# TEST HASH ID WITH

    curl -X POST -H "Content-Type: application/json" -d '{"data":"example"}' http://localhost:6000/generate/hash

