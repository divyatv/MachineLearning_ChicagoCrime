from flask import Flask, jsonify, render_template
import json
import pandas as pd
import numpy as np
import os

## Read The CSV File ###
app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/mapplot', methods=['GET','POST'])
def scrapedmap():
    
    crime_df_for_2018 = pd.read_csv("resources/Chicago2018dataforplots.csv")
    ## Chose the crime type from the dropdown and assign it to a variable
    Primary_Type = 'THEFT'

    # Filter the Dataframe using the crime type
    filtered_ptype_data = crime_df_for_2018.loc[(crime_df_for_2018["Primary Type"]== Primary_Type) & (crime_df_for_2018["Arrest"] == 1), ["Primary Type", "Arrest", 'Police Beats', "Ward", "Police Districts", "Latitude", "Longitude"]]

    renamed_df = filtered_ptype_data.rename(columns={"Primary Type": "Primary_Type", "Police Beats": "Police_Beats", "Police Districts":"Police_Districts"})

    return render_template("Marker_Clusters.html", jsonvalue= json.dumps(renamed_df.to_dict('records')))
    # return render_template("Marker_Clusters.html")

if __name__ == "__main__":
    app.run()
