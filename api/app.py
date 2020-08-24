from flask import Flask, request
from .firebase import getDB as db
import json
from .coffeeShops.Richmond.Lamplighter.lamplighterOrder import lamplighterOrder
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/drinks')
def getDrinks():
    drink = db.getDrink(request.args.get('city'), request.args.get('location'), request.args.get('drink'))
    return drink

@app.route('/order')
def placeOrder():
    city = request.json.get('city')
    location = request.json.get('location')
    order = request.json.get('order')

    if city == 'Richmond':
        if location == 'Lamplighter':
            ordered = lamplighterOrder(order)
            return ordered
        elif location == 'Blanchards':
            print("Call Blanchards Order")
    elif city == 'Charlottesville':
        print("similar logic for other city")

