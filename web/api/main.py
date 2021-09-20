import uvicorn
from fastapi import FastAPI
from datadog import initialize, statsd
import os

app = FastAPI()
initialize(statsd_host=os.environ.get('DATADOG_HOST'))
statsd.service_check(
    check_name="application.service_check",
    status="0",
    message="Application is OK",
)

@app.get("/")
def read_root():
    statsd.increment('api.new_request')
    return {"ping": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")