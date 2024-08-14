# S3 Fastapi
Expose Swagger Inferface For Compatible S3 endpoint
v0.1

## How it works?
Exposing Swagger Interface for S3 to list/put/remove buckets/objects.
Runs awscli commands on the background and expose it via HTTP
output object based on AWS Configure command (recommend using json)

## Requirements
awscli package installed
python3.11 -m pip install fastapi uvicorn

## functions
* list_bucket_objects

### How to use
  use "aws configure" to configure profile with access/secret keys
  then run fastapimain.py that expose Swagger web UI on that server via port 8000 (all of this can be change inside py file in main function
  access doc swagger using browser and surf to "http://<server-ip>:8000/docs" or "http://<server-ip>:8000/docs"

# USES
1. by itself 
2. via every Web UI that can run HTTP command and get json object back (same as python requests)

## Test
for now, tested on compatible s3 server without ssl, and uses python3.11
  ALL RIGHT RESERVER ## USE WITH CAUTION
