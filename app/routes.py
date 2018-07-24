from flask import render_template, request, url_for, redirect, flash
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/founders')
def founders():
    return render_template("founders.html")

@app.route('/technology')
def technology():
    return render_template("technology.html")

@app.route('/pipeline')
def pipeline():
    return render_template("pipeline.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/otheroptions')
def otheroptions():
    return render_template("otheroptions.html")

@app.route('/caveat_lector')
def caveat_lector():
    return render_template("caveat_lector.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/services/vscreen')
def vscreen():
    return render_template("vscreen.html")

@app.route('/services/libdesign')
def libdesign():
    return render_template("libdesign.html")

@app.route('/successstories')
def successstories():
    return render_template("successstories.html")

@app.route('/successstories/ptp1b')
def ptp1b():
    return render_template("ptp1b.html")

@app.route('/successstories/ampc')
def ampc():
    return render_template("ampc.html")

@app.route('/successstories/model')
def model():
    return render_template("model.html")

@app.route('/successstories/tm0936')
def tm0936():
    return render_template("tm0936.html")

@app.route('/contact/affiliates')
def affiliates():
    return render_template("affiliates.html")