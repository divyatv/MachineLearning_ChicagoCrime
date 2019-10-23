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

@app.route('/', methods=['GET'])
def dropdown():
    crimes = ['battery', 'narcotics', 'burglary', 'damage','other','theft']
    return render_template('main.html', crimes=crimes)

if __name__ == "__main__":
    app.run(host='localhost', port= 5001)

