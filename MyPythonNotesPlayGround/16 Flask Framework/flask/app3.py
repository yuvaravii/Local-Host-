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
def get_items():
    return jsonify(items_dict_list)

if __name__ == "main":
    app.run(debug = True)
