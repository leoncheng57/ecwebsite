from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/apply")
def apply():
    return render_template("apply.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "adashljdoiqdm"
    app.run('0.0.0.0',port=8000)
