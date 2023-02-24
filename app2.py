from flask import Flask, request
import requests, json

app = Flask(__name__)

@app.route("/calltheapi")
def calltheapi():
    dict1 = requests.get("http://localhost:5000/getweap").json()
    print(type(dict1))
    weap = dict1["weapon"]
    status = dict1["status"]
    damage = dict1["damage"]
    # status = requests.get("http://localhost:5000/getstatus").text
    # dam = requests.get("http://localhost:5000/getdam").json()
    return f"{weap} of {status}: {damage}"

# @app.route("/callthepostapi")
# def callthepostapi():
#     res = requests.post("http://localhost:5000/post").text
#     return f"{res} was the result retrieved from the API"

# @app.route("/calltheputapi", methods = ["POST"])
# def calltheputapi():
#     dict1 = request.get_json()
#     res = requests.put("http://localhost:5000/putordel").json()
#     result = dict1["name"]
#     return f"{res} was the result retrieved from the API. {result}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)