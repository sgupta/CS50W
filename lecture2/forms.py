from flask import Flask, render_template, request

#create app object
app = Flask(__name__)

#call route method from object app
@app.route("/")
def forms():
    return render_template("forms.html")

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello"

@app.route("/printname", methods=["POST"])
def printname():
    name = request.form.get("name")
    name = name.capitalize()
    return render_template("printname.html", name=name)

if __name__ == "__main__":
    app.run()