import os
from flask import Flask, render_template
from src.variables import OS_KEY

app = Flask(__name__)

properties = []

app.secret_key = os.getenv("SESSION_SECRET_KEY")

@app.route("/")
def login():
    return render_template("home.html", key=OS_KEY)

@app.route("/<int:uprn>")
def property(uprn):
    
    prop = None
    for property in properties:
        if property.uprn == uprn:
            prop = property 
            break
        
    return render_template("property.html", property=prop, key=OS_KEY)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
