# S3 Fastapi
Expose Swagger Inferface For S3 endpoint

## How it works?
Exposing Swagger Interface for S3 to list/put/remove buckets/objects.
Runs awscli commands on the background and expose it via HTTP
output object based on AWS Configure command (recommend using json)

## Requirements
awscli package installed
### v0.1
  use "aws configure" to configure profile with access/secret keys
  then run fastapimain.py that expose Swagger web UI on that server via port 8000 (all of this can be change inside py file in main function
  access doc swagger using browser and surf to "http://<server-ip>:8000/docs" or "http://<server-ip>:8000/docs"

# USES
1. by itself
2. via every Web UI that can run HTTP command and get json object back (same as python requests)

  ALL RIGHT RESERVER ## USE WITH CAUTION
