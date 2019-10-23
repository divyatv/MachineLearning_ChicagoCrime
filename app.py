from flask import Flask, jsonify, render_template, json

from flask import request, redirect, Response, url_for, make_response
import random

import io

app = Flask(__name__)

###############################################################
# Flask server for data extraction and rendering html
###############################################################
# 

#### Main route ############################################################################################
@app.route("/")
def home():
    """Return the homepage with a plot for team"""
    return(render_template("index.html"))
    #return("Hello world")

app.run(host='localhost', port= 5001)
