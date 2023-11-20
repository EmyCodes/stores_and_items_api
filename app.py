#!/usr/bin/python3

from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
			}
		]
	}
]

@app.get("/store")
def get_stores():
    return [{"stores": stores}]

@app.post("/store")
def create_stores():
    request_store = request.get_json()
    new_store = {"name": request_store["name"], "items": request_store["items"]}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/items")
def create_item(name):
    new_item = request.get_json()
    for store in stores:
        if store == name:
            new_store = {"name": new_item["name"], "items": new_item["items"]}
            return new_store, 201
    return f"Message: {name} not found", 401