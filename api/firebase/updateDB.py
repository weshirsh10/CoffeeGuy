import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./cg_fb_creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

item = {
    "BlackEye": {
    "name": "Black Eye",
    "description": "hot batch brewed coffee or cold brew with a double shot of espresso added",
    "drink": True,
    "type": {
        "iced": True,
        "hot": True,
        "Espresso": True,
        "extraEspresso": True,
        "steamedMilk": False
    },
    "xpath": "/html/body/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div",
    "sizes": {
        "8ozHot": 3,
        "12ozHot": 3.5,
        "20ozHot": 4.5,
        "12ozIced": 3.75,
        "16ozIced": 4.25,
        "20ozIced": 4.75
    },
    }
}

def addDrink(city, location, item):
    items = db.collection("coffeeShops").document(city).collection(location).document("items").update(item)
    print("done", items)

addDrink("Richmond", "Lamplighter", item)