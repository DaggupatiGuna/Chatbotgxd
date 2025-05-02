from fastapi import FastAPI
from analytics import current_inventory_levels, predictive_inventory_shortage

app = FastAPI()

@app.get("/current_inventory")
def current_inventory():
    return {"inventory": current_inventory_levels()}

@app.get("/predictive_inventory")
def predictive_inventory():
    return {"predictive_inventory": predictive_inventory_shortage()}
