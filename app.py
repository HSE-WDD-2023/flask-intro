from flask import Flask, render_template, request

# creates an applicaiton from this file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    # grab the value of the name key from the url
    name = request.args.get("name", "Royals")
    return render_template("hello.html", name=name)

@app.route("/goodbye")
def goodbye():
    name = request.args.get("name")
    return render_template("goodbye.html", name=name)

