from flask import Flask, render_template

app = Flask('application')

@app.route("/")
def index():
    message="Subhash Gupta Flasks app"
    return render_template("index.html", message=message)

@app.route("/subhash")
def subhash():
    return "Hello, Subhash"

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run()