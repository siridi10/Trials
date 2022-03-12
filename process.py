import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/nakstra')

def nakstra(n):
    if n>27:
        print("Invalid Nakshtra Number")
    return (naks[n-1])
naks=["Ashvini",
"Bharani",
"Krittika",
"Rohini",
"Mrigashīrsha",
"Ardra",
"Punarvasu", 
"Pushya",
"Āshleshā",
"Maghā",
"Pūrva Phalgunī",
"Uttara Phalgunī",
"Hasta",
"Chitra",
"Swati",
"Vishakha",
"Anuradha",
"Jyeshtha",
"Mula",
"Purva Ashadha",
"Uttara Ashadha",
"Sravana",
"Dhanishta",
"Shatabhisha",
"Purva Bhadrapada",
"Uttara Bhādrapadā",
"Revati"]
n=int(input("Enter the Nakshtra number "))
nakstra(int(n))


if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()