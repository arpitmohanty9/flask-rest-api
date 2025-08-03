from flask import Flask, request
from db import stores, items

app = Flask(__name__)

#stores data store
# stores = [
#     {
#         "name": "My Store",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
#     }
# ]
# we will use dict for stores and dict for items


@app.get("/store")
def get_store():
    return {"stores" : stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items":[] 
                 }
    stores.append(new_store)
    return new_store,201

@app.post("/store/<string:name>/item")
def add_items(name):
    request_data = request.get_json()

    item = {
        "name":request_data["name"],
        "price":request_data["price"]
    }
   
    for store in stores:
        if store["name"] == name:
            store["items"].append(item)
            return store,201

    return {"message": "Store not found"},404

#stupid way of doing things
# @app.get("/store/<string:store_id>")
# def get_specific_store(store_id):
#     if stores[store_id]:
#         return stores[store_id]
#     return {"message" : "store not found"}, 404

@app.get("/store/<string:store_id>")
def get_specific_store(store_id):
    if stores[store_id]:
        return stores[store_id]
    return {"message" : "store not found"}, 404