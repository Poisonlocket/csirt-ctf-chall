from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Cookie dispenser Service for Ducks. Sadly we dont have enough funding yet to afford a Frontend Dev. Our Backend engineer also was kind of underpaid so we hope he did his job right and didnt leave any vulnerabilitys. Anyways, head to /cookie for a free cookie, if you dont get one, an admin needs to refill them at /admin"}

@app.get("/cookie")
def cookie():
    return {"message": "hemlo cookie"}

@app.api_route("/admin")
def admin():
    return {"message": "yes"}

@app.get("/admin")
def admin():
    return {"message": "yes"}
