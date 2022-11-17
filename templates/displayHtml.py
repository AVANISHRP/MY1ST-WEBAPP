from flask import Flask,render_template

app = Flask(__name__)
@app.route("/app")
def studentWEbPage():
    name = "Avanish"
    return render_template("Web.html", student_name = name)
app.run(debug = True)