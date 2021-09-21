import uvicorn
from fastapi import FastAPI
from routes import helpers, users
app = FastAPI()

app.include_router(helpers.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")