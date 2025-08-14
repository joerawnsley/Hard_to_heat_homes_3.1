from flask import Flask, render_template, request, redirect, url_for
from src.os_api import os_api_call
from src.utils import get_properties_from_os, setting_void_properties, get_attributes_from_epc
from src.variables import OS_KEY
from src.council_data_utils import get_bbox_for_council_code, filter_properties_by_council_code

app = Flask(__name__)

properties = []
council_code = ""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        global council_code
        council_code = request.form.get("council")
        return redirect(url_for("home"))
    return render_template("login.html")

def change_council_code():
    #update council code
    #call load properites
    return

def load_properties(council_code):
    council_bbox = get_bbox_for_council_code(council_code)

    HEADERS = {"Accept": "application/json"}
    PARAMS = {
        "key": OS_KEY,
        "filter": "buildinguse_oslandusetiera = 'Residential Accommodation' AND mainbuildingid_ismainbuilding = 'Yes'",
        "bbox": council_bbox,
         }

    #global properties
    if len(properties) == 0:
        list_of_buildings = os_api_call(HEADERS, PARAMS)["features"]
        properties = get_properties_from_os(list_of_buildings)
        properties = filter_properties_by_council_code(council_code, properties)
        properties = get_attributes_from_epc(properties)
        
        for i in range(len(properties)):
            properties[i].calculate_score()

@app.route("/home")
def home():
    
    global council_code
    
        
    return render_template("home.html", properties=properties, key=OS_KEY)

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
