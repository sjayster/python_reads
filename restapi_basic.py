"""
Making use of the Flask module to create and define the routes
The json file is stored in my local workspace. Same location as this application.route

Steps:

1. Installed Flask
2. The http request will be sent to http://127.0.0.1:5000/, which is the localhost

"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask import make_response
import json
import unittest

"""
We define our Flask app and load the json file to a list of dictionary, d
"""

app = Flask("First app")
f = open("evaluations.json")
d = json.load(f)
f.close()

"""
Error handling:
I am using flask_restful to handle the 404 errors.
For 500 error codes, I am using the make_response module in the flask library
"""

api = Api(app, catch_all_404s=True)


@app.errorhandler(500)
def badrequest(error="Must be an incorrect query. Please check. Go to http://127.0.0.1:5000/ for the homepage"):
    return make_response(jsonify({'Error': error}), 500)


@app.route('/', methods=['GET'])
def api_root():
    return "Welcome to Twilio's flask app"

"""
1. The following function takes care of the following requirements
http://localhost:8080/api/evaluations is defined for the route 
http://localhost:8080/api/evaluations?product_group=:product_group_name
2. request.args catches any additional arguments passed to the above URL
3. If there are no args, we just print the json file
   If not, we check to see what the key and value is.
4. Depending on the key and value pair, the json file is parsed accordingly using list comprehension.
"""


@app.route('/api/evaluations', methods=['GET'])
def productgroup():
    arguments = request.args
    if not arguments:
        return jsonify(d)
    for k, v in arguments.items():
        groupkey = k
        groupval = v
    output = [items for items in d if items[groupkey] == groupval]
    return jsonify(output)


"""
1. The following function takes care of the following requirements
http://localhost:8080/api/stats?metrics=grade,status&group_by=product_group
2. request.args catches the additional arguments passed to the above URL
3. If there are no args, we just print the json file
4. If not, we check to see if "group_by" is present in the arguments dictionary and set gpr flag to True
5. Similarly, we do the same for metrics and set the mtcs flag to True
6. First, we get the list of grouper key elements -> say, group_by = "product_group" 
This is stored in a list called shorted with the unique "product_group" values.
We use this list to go over all the products in a product group
7. The status is stored in a statuscodes dictionary with key as the status and value as 1 to 4
8. We iterate over the shorted list and get all the products for the key
9. We then iterate over the metric and get the element with the least metric value and store it to answer dictionary
10. Once we get the least of all metrics, we add the answer dictionary to the anslist list, so that we can jsonify it
11. Return jsonify(anslist)
"""


@app.route('/api/stats', methods=['GET'])
def ranking():
    arguments = request.args
    gpr = False
    mtcs = False
    if not arguments:
        return jsonify(d)
    if arguments:
        if "group_by" in arguments:
            grouper = arguments["group_by"]
            gpr = True
        if "metrics" in arguments:
            vals = arguments["metrics"]
            metric = vals.split(',')
            mtcs = True

    # First, we get the list of grouper key elements -> say, group_by = "product_group"
    # This is stored in a list called shorted with the unique "product_group" values.
    # We use this list to go over all the products in a product group

    possible_keys = d[0].keys()
    if grouper not in possible_keys:
        return badrequest("Key %s does not exist" % (grouper))

    shorted = list(set([l[grouper] for l in d]))
    statuscodes = {"not_started": 1, "self_assessment": 2,
                   "pending_approval": 3, "complete": 4}
    anslist = []
    for elements in shorted:
        answer = {}
        if gpr:
            grouped = [elts for elts in d if elts[grouper] == elements]
        if not mtcs:
            return jsonify(d)
        if mtcs:
            for m in metric:
                output = sorted(grouped, key=lambda k: k[m])
                if output:
                    answer[grouper] = output[0][grouper]
                    newmetric = output[0][m]
                    answer[m] = newmetric
            anslist.append(answer)
    return jsonify(anslist)

if __name__ == '__main__':
    app.run()
