from flask import Flask, jsonify, render_template, json

import csv
import pandas as pd
import os
from matplotlib import pyplot as plt
import time
import numpy as np
from textwrap import wrap
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Layout

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

###############################################################
# Flask server for data extraction and rendering html
###############################################################
# 

#### Main route ############################################################################################
@app.route("/")
def home():
    """Return the homepage with a plot for team"""
    return render_template("homepage.html")
   
##### Harsha's code #####
@app.route("/beat/<type_crime>")
def beat_plot(type_crime):
    ## Read The CSV File ###
    crime_df_for_2018 = pd.read_csv("Resources/Chicago2018dataforplots.csv")

    ## Chose the crime type from the dropdown and assign it to a variable
    Primary_Type = type_crime

    # Filter the Dataframe using the crime type
    filtered_ptype_data = (crime_df_for_2018.loc[crime_df_for_2018["Primary Type"]== Primary_Type, ["Primary Type", "Arrest", 'Police Beats', "Ward", "Police Districts", "Latitude", "Longitude"]]).rename(columns = {'Police Beats':'Police_Beats','Police Districts':'Police_Districts'})

    # Create a Pivot Table to determine efficiency of a Police Beat
    beat_eff_pivot = (filtered_ptype_data.pivot_table(index=['Police_Beats'], columns='Arrest', aggfunc='size', fill_value=0)).reset_index()

    # Create a Pivot Table to determine efficiency of a Police District
    district_eff_pivot = (filtered_ptype_data.pivot_table(index=['Police_Districts'], columns='Arrest', aggfunc='size', fill_value=0)).reset_index()

    # Get the top police beats based on efficiency
    beat_arrestcount = beat_eff_pivot[[0, 1]].sum(axis=1)
    beat_eff_pivot['Beat_Efficiency'] = (beat_eff_pivot[1] / beat_arrestcount) * 100

    # Get the top police districts based on efficiency
    district_arrestcount = district_eff_pivot[[0, 1]].sum(axis=1)
    district_eff_pivot['District_Efficiency'] = (district_eff_pivot[1] / district_arrestcount) * 100

    # Get Top 5 Beats and Districts based on efficiency
    top5_beats_dict = (beat_eff_pivot.sort_values(by='Beat_Efficiency', ascending=False).head(5)[['Police_Beats','Beat_Efficiency']]).to_dict('records')
    top5_districts_dict = (district_eff_pivot.sort_values(by='District_Efficiency', ascending=False).head(5)[['Police_Districts','District_Efficiency']]).to_dict('records')


    merged_dict = [{**beat,**top5_districts_dict[row]} for row,beat in enumerate(top5_beats_dict)]

    return merged_dict
#####################################################################################   


############################################################################################################
### Running main function
if __name__ == "__main__":
    app.run(debug=True)
####################################################################################################