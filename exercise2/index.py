from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def exercise2():
    return render_template("index.html")