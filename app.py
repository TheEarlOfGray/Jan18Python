from flask import Flask, request, jsonify
from random import choice, randint

app = Flask(__name__)

weaplist = ["sword", "spear", "dagger", "bow"]
statuslist = ["fire", "frost", "might", "slow"]

@app.route("/getweap")
def getweap():
    dict1 = {"weapon": choice(weaplist), "status": choice(statuslist), "damage": randint(10, 100)}
    return jsonify(dict1)

# @app.route("/getstatus")
# def getstatus():
#     return choice(statuslist)

# @app.route("/getdam")
# def getdam():
#     return jsonify(randint(10, 100))
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)