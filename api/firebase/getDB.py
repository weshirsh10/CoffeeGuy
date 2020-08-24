import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase/cg_fb_creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getDrink(city, location, drink):
    drinkMap = db.collection("coffeeShops").document(city).collection(location).document("drinks").get().to_dict()
    return drinkMap.get(drink)

