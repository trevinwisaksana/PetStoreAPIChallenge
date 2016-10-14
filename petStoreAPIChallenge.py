# Imported Flask class
from flask import Flask, jsonify, url_for
# Imported Request methods
from flask import request
# Imported JSON
import json

''' Create a simple Flask web server that receives GET requests
    to the route `/hello` and responds with a friendly message.
    Test this route in your web browser and using Curl, Postman,
    or another tool to make HTTP requests.  '''


''' Creating an instance of Flask class.
    The first argument is the module
    or package name. '''
app = Flask(__name__)


# Challenge 2
@app.route('/hello')
# GET request to say "Hello World"
def hello_world():
    return 'Hello, World!'

# Will contain list of JSON data
listOfJSON = []


# Challenge 3
@app.route('/pets', methods=['POST'])
# POST request with JSON data in the body
def pets():
    # input_json is a list of all the keys
    input_json = request.get_json(force=True)
    # force=True, above, is important to not silently fail
    # Checking if the keys name, age and species exist.
    if "name" in input_json.keys() and "age" in input_json.keys() and "species" in input_json.keys():
        # Appends json data with type string to the listOfJSON
        listOfJSON.append(input_json)
        return "input_json appended to listOfJSON"
    print("Error, could not append input_json to listOfJSON")
    return "Something is wrong"


# Challege 4
@app.route('/pets', methods=['GET'])
def petGetRequest():
    # Used to contain the converted dictionary into strings.
    return_list = []
    # Loops through every element in the listOfJSON array
    for i in listOfJSON:
        # Appending the converted JSON into string into the list
        return_list.append(json.dumps(i))
    # Seperating each dictionary in array using ','
    return ','.join(return_list)


# Challenge 5
@app.route('/pets/<name>', methods=['GET'])
def petNameGetRequest(name):
    for i in listOfJSON:
        # If the dictionary with the key name is equal to the name "Nyan Cat"
        if name == i["name"]:
            # Return the string version of that dictionary
            return json.dumps(i)
    return "No name can be matched."

if __name__ == '__main__':
    app.run(debug=True)
