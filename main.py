from flask import Flask, render_template

app = Flask('SuperScrapper')

@app.route('/')
def home():
    return "Hello! Welcome to song"

@app.route("/contact")
def contact():
    return "Contact me"

@app.route("/<username>")
def hello_name(username):
    return f"Hello your name is {username}"


@app.route("/job")
def search_job():
    return render_template("index.html")




app.run()
