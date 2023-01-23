from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"Home page"

@app.route("/about")
def about():
    return f"Some info"

@app.route("/help/<int:num>")
def help(num):
    return f"{num * 5}"

@app.route("/contact")
def contact():
    return f"Don't contact me."

if __name__ == "__main__":
    app.run(port=5000, debug=True)