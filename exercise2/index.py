from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def exercise2():
    return render_template("index.html")

@app.route("/calculate", methods=['GET', 'POST'])
def calc():
    good_input = True
    num = request.form.get("number")
    if num.isdigit() == False and num != '':
        good_input = False
        return render_template("calculate.html", number=0, inp=good_input)
    elif num.isdigit() == False:
        good_input = False
        return render_template("calculate.html", number=1, inp=good_input)
    else:
        num = int(request.form.get("number"))
        return render_template("calculate.html", number=num, inp=good_input)