from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def exercise3():
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def register():
    return render_template("index.html")
