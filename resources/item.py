import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items,stores


blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/store/<string:item_id>")
class Item(MethodView):
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")


    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self,item_id):
        item_data = request.get_json()
        # Here not only we need to validate data exists
        # But also what tyoe of data. Price should be a float.
        # for example
        
        
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad Request, ensure 'price' and 'name' are included in JSON playload")
    
        try :
            item = items[item_id]
            # dictionary-merge-update-operators
            item |= item_data
            return item
        except KeyError:
            abort(404,"Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"Items" : list(items.values())}
    
    def post(self):
        item_data = request.get_json()
        # check for params
        if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
            abort(400, message="Bad Request, ensure 'price','store_id' and 'name' are include in JSON playload")
        

        for item in items.values():
            if(
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exist")

        # if item_data["store_id"] not in stores:
        #     abort(404,message="Store not found.")
        
        item_id = uuid.uuid4().hex
        item = {
            **item_data,
            "id":item_id
            }
        items[item_id] = item

        return item


    