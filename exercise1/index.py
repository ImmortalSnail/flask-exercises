from flask import Flask, render_template
import datetime
from datetime import datetime


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    time = str(datetime.now())[:19]
    return render_template("index.html", time=time)