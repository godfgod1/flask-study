from flask import Flask, render_template, request,redirect,send_file
from scrapper import get_jobs
from exporter import save_to_file


app = Flask('SuperScrapper')

db = {}

# @app.route('/')
# def home():
#     return "Hello! Welcome to song"

@app.route("/contact")
def contact():
    return "Contact me"

@app.route("/<username>")
def hello_name(username):
    return f"Hello your name is {username}"


@app.route("/")
def search_job():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = []
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/job")
    return  render_template('report.html',searchBy =word, resultNumber=len(jobs), jobs=jobs)
    # print(request.args)
    # return f'this is the react'

@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect('/')

app.run()







