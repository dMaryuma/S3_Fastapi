from fastapi import FastAPI, Query, HTTPException
import subprocess
import json

app = FastAPI()

@app.get("/list_all_buckets/")
async def list_all_buckets():
    return None

@app.get("/list_objects/")
async def list_objects(
    endpoint_url: str = Query(..., description="The S3 endpoint URL"),
    bucket: str = Query(..., description="The name of the S3 bucket"),
    prefix: str = Query(None, description="Prefix to filter objects by"),
    max_keys: int = Query(1000, description="Maximum number of keys to return"),
    no_verify_ssl: bool = Query(True, description="Disable SSL verification")
):
    command = [
        "aws", "s3api", "list-objects-v2",
        "--endpoint-url", endpoint_url,
        "--bucket", bucket,
        "--max-keys", str(max_keys),
        "--output", "json"
    ]

    if prefix:
        command.extend(["--prefix", prefix])
    if no_verify_ssl:
        command.append("--no-verify-ssl")

    try:
        # Run the AWS CLI command
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Command failed: {stderr.decode().strip()}")

        # Parse the output as JSON
        json_output = json.loads(stdout.decode())

        # Return the parsed JSON object
        return json_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
