import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase/cg_fb_creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getItem(city, location, item):
    itemMap = db.collection("coffeeShops").document(city).collection(location).document("items").get().to_dict()
    return itemMap.get(item)

