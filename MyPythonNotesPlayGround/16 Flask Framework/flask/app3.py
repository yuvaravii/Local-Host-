### use put or delete  -- HTTP verbs
## Working with different API -- JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

## creating initial items for the to do list
items_dict_list = [
    {'id' : 1, "name" : "Task1", "description" : "Short description of task1"},
    {'id' : 2, "name" : "Task2", "description" : "Short description of task2"},
    {'id' : 3, "name" : "Task3", "description" : "Short description of task3"}
]

@app.route("/")
def home():
    return "Welcome the to the sample To-Do List App "

## get all the items within the app
@app.route("/items",methods =["GET"])
def get_all_items():
    return jsonify(items_dict_list)

## get the items with respect id requested 
@app.route("/items/<int:item_id>",methods = ["GET"])
def get_id_specific_item(item_id):
    id_specific_item = next((item for item in items_dict_list if item["id"] == item_id),None)
    if id_specific_item is None:
        return jsonify({"error":"item is missing"}) 
    else: 
        return jsonify(id_specific_item)
    
## writing scripts for creating new item list
@app.route("/items", methods = ["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"error":"item is missing"}) 
    else:
        new_item = {
            "id" : items_dict_list[-1]["id"] if items_dict_list else 1,
            "name" : request.json["name"],
            "description" : request.json["description"]
            }
    items_dict_list.append(new_item)
    return jsonify(new_item)

## put method is used for updating the existing value within the dictionary
@app.route("/items/<int:item_id>",methods = ["PUT"])
def update_item(item_id):
    fetched_item = next((item for item in items_dict_list if item["id"] == item_id),None)
    if fetched_item is None:
        return jsonify({"error":"Item is missing"})
    fetched_item["name"] = request.json.get("name", items_dict_list["name"])

    return jsonify(fetched_item)

if __name__ == "__main__":
    app.run(debug=True)
