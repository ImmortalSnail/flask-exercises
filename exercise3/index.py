from flask import Flask, render_template, request



app = Flask(__name__)
dict = {}

@app.route("/", methods=['GET', 'POST'])
def exercise3():
    return render_template("index.html")

@app.route("/registration", methods=['GET', 'POST'])
def register():
    name = request.form.get("name")
    club = request.form.get("club")
    dict[name] = club

    return render_template("registration.html", dict=dict)
