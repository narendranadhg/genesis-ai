from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
    "company": "Genesis AI",
    "product": "Atlas",
    "status": "Development Started",
    "founder": "Narendranadh G",
    "version": "0.0.1"
    }