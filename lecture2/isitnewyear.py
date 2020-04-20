import datetime
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def isitnewyear():
    now = datetime.datetime.now()
    if now.month == 1 and now.date == 1:
        new_year = True
    else:
        new_year = False
    return render_template("newyear.html", new_year = new_year)

if __name__ == "__main__":
    app.run()
