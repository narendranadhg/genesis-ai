from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "company": "Genesis AI",
        "product": "Atlas"
    }

@app.get("/about")
def about():
    return {
        "founder": "Narendranadh G",
        "vision": "Build Enterprise AI Solutions"
    }

@app.get("/version")
def version():
    return {
        "version": "0.0.1",
        "environment": "development"
    }

@app.get("/Profile")
def profile():
    return {
        "name": "Narendranadh G",
        "role": "Founder",
        "company": "Genesis AI",
        "skills": [
            "SAP BW",
            "Python",
            "FastAPI"
        ]
    }