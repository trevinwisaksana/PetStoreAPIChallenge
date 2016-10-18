# Imported Flask class
from flask import Flask, jsonify, url_for
# Imported Request methods
from flask import request
# Imported JSON
import json

''' Creating an instance of Flask class.
    The first argument is the module
    or package name. '''
app = Flask(__name__)


# Challenge 2
@app.route('/hello')
# GET request to say "Hello World"
def hello_world():
    return 'Hello, World!'


# Contain list of JSON data
listOfJSON = []


# Challenge 3 and 6
@app.route('/pets', methods=['POST'])
# POST request with JSON data in the body
def pets():
    # input_json is a list of all the keys
    input_json = request.get_json(force=True)
    name = input_json['name']
    # force=True, above, is important to not silently fail
    # Checking if the keys name, age and species exist.
    if 'name' in input_json.keys() and 'age' in input_json.keys() and 'species' in input_json.keys():
        # Iterates through the listOfJSON
        for i in listOfJSON:
            if name == i['name']:
                # If the name is the same, it will not allow the data to be added
                return "HTTP 409 ERROR: NAME IS NOT UNIQUE"
        # Appends json data with type string to the listOfJSON
        listOfJSON.append(input_json)
        return "input_json appended to listOfJSON"
    return "HTTP 409 Error."

''' # Check if the key "name", "age" and "species" exist.
    # If it exists, check if the value of the name is equal to any value of the name in the listOfJSON
        # If a value of a name matches with any on the list
            # Print "Error 404"
        # If the name is not the same with any names
            # Append the JSON data to the listOfJSON '''


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
    return "No names can be matched."


# Challenge 7
@app.route('/pets/<name>', methods=['PUT'])
def replacePet(name):
    # input_json is a list of all the keys
    input_json = request.get_json(force=True)
    # Iterates through the listOfJSON
    numberOfElements = listOfJSON.count
    # for i in listOfJSON:
    for i in listOfJSON:
        # Checks if any of the name matches any on the list
        if name == i['name']:
            listOfJSON.update(input_json)
    return "HTTP 404 ERROR: NAME DOES NOT EXIST"


if __name__ == '__main__':
    app.run(debug=True)
