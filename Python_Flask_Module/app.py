from flask import Flask, render_template, request, jsonify, json
from flask import send_file
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import SelectField

import csv
import numpy as np
import json
import pandas as pd
import os
from matplotlib import pyplot as plt
import time
from textwrap import wrap
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Layout

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
#app= Flask(__name__, template_folder= '' )

###########################################################################
###############################################################
# Flask server for data extraction and rendering html
###############################################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret'

#### Main route ############################################################################################
@app.route("/")
def home():
    """Return the homepage with a plot for team"""
    return render_template("index.html")

############################################################################################################
#     
class Form(FlaskForm):
    crime = SelectField('crime', choices=[('ba', 'battery'), ('bu','burglary'), \
                ('da','damage'), ('n','narcotics'), ('o','other'), ('t', 'theft', )]) 
    plot = SelectField('plot', choices=[('pl','plain'), ('he','hexbin'),  \
                                    ('sb', 'seaborn-box'), ('sp','seaborn-pair')])

@app.route("/plot", methods=['GET', 'POST'])
def index():
    form = Form()
    crime_dic = {'ba':'battery', 'bu':'burglary', 'da':'damage', \
                 'n':'narcotics', 'o':'other', 't':'theft' }
    plot_dic = {'pl':'', 'he':'hexbin', 'sb':'seaborn-box', 'sp':'seaborn-pair'}

    if request.method == 'POST':
        plot = form.plot.data
        crime = form.crime.data
        print('crime=', form.crime.data, " len=", len(crime))
        print('plot=', form.plot.data)
        if plot == 'pl':
            filename = 'static/' +  crime_dic[crime] + '.png'
        else:
            filename = 'static/' +  crime_dic[crime] + '-' + plot_dic[plot] +'.png'
        print("filename=", filename)
        return send_file(filename, mimetype='image/jpg')

    return render_template('plot.html', form=form)
############################################################################################################# 
from flask import render_template
from bokeh.embed import file_html
from bokeh.plotting import figure
from bokeh.resources import CDN

@app.route('/gmplot', methods=['GET'])
def example():

    plot = figure()
    plot.circle([1,2], [3,4])

    html = file_html(plot, CDN)

    return render_template('crime_datadf4_PR3.html', plot=html)
#########################################################################################################
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
########################################################################################################
@app.route("/googlemap")
def gmap():
    """Return the googlemap  with a plot for team"""
    return render_template("googlemap.html")
   
##### Get crime count for each year #############################################################################
@app.route("/count/<crime_type>")
def count_result(crime_type):

    #print("Crime Type:", crime_type)

    #read the csv file
    file = os.path.join('selected_crime_data.csv')
    crime_df = pd.read_csv(file)

    # Filter data based on type of crime and year selected
    crime_2010_df = crime_df.loc[crime_df['Year'] == 2010]
    crime_2011_df = crime_df.loc[crime_df['Year'] == 2011]
    crime_2012_df = crime_df.loc[crime_df['Year'] == 2012]
    crime_2013_df = crime_df.loc[crime_df['Year'] == 2013]
    crime_2014_df = crime_df.loc[crime_df['Year'] == 2014]
    crime_2015_df = crime_df.loc[crime_df['Year'] == 2015]
    crime_2016_df = crime_df.loc[crime_df['Year'] == 2016]
    crime_2017_df = crime_df.loc[crime_df['Year'] == 2017]
    crime_2018_df = crime_df.loc[crime_df['Year'] == 2018]

    #Sift through the data to classify by "crime type"   
    crime_2010 = crime_2010_df.loc[crime_2010_df['Primary Type'] == crime_type]
    count_2010 = int(crime_2010["Primary Type"].count())
    crime_2011 = crime_2011_df.loc[crime_2011_df['Primary Type'] == crime_type]
    count_2011 = int(crime_2011["Primary Type"].count())
    crime_2012 = crime_2012_df.loc[crime_2012_df['Primary Type'] == crime_type]
    count_2012 = int(crime_2012["Primary Type"].count())
    crime_2013 = crime_2013_df.loc[crime_2013_df['Primary Type'] == crime_type]
    count_2013 = int(crime_2013["Primary Type"].count())
    crime_2014 = crime_2014_df.loc[crime_2014_df['Primary Type'] == crime_type]
    count_2014 = int(crime_2014["Primary Type"].count())
    crime_2015 = crime_2015_df.loc[crime_2015_df['Primary Type'] == crime_type]
    count_2015 = int(crime_2015["Primary Type"].count())
    crime_2016 = crime_2016_df.loc[crime_2016_df['Primary Type'] == crime_type]
    count_2016 = int(crime_2016["Primary Type"].count())
    crime_2017 = crime_2017_df.loc[crime_2017_df['Primary Type'] == crime_type]
    count_2017 = int(crime_2017["Primary Type"].count())
    crime_2018 = crime_2018_df.loc[crime_2018_df['Primary Type'] == crime_type]
    count_2018 = int(crime_2018["Primary Type"].count())    
   
    year = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']      

    # specify an array crime_count
    crime_count = [count_2010, count_2011, count_2012, count_2013, count_2014, count_2015, count_2016, count_2017, count_2018]    
    # define a dataframe using the above
    crime_dict = {'Crime Count':crime_count,'Year':year}
    # convert the above to tuples (zipping the data in the required format)
    mod_result = [{"Crime Count":i, "Year":b} for i, b in zip(crime_dict["Crime Count"], crime_dict["Year"])]
    final_result = json.dumps(mod_result)
    return final_result

########################################################################################################

############################################################################################################
### Running main function
if __name__ == "__main__":
    app.run(debug=True)
####################################################################################################




