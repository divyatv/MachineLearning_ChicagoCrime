from flask import Flask, render_template, request, jsonify
from flask import send_file
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import SelectField

from flask import Flask, jsonify, render_template, json

import csv
import pandas as pd
import os
from matplotlib import pyplot as plt
import time
from textwrap import wrap
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Layout

#app = Flask(__name__)
#app = Flask(__name__, static_url_path='/static')
app= Flask(__name__, template_folder= '' )

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
   
##### Get status of the stock #############################################################################
@app.route("/count/<crime_type>")
def count_result(crime_type):

    #print("Crime Type:", crime_type)

    #read the csv file
    file = os.path.join('selected_crime_data.csv')
    crime_df = pd.read_csv(file)

    # Filter data based on type of crime and year selected

    crime_2001_df = crime_df.loc[crime_df['Year'] == 2001]
    crime_2002_df = crime_df.loc[crime_df['Year'] == 2002]
    crime_2003_df = crime_df.loc[crime_df['Year'] == 2003]
    crime_2004_df = crime_df.loc[crime_df['Year'] == 2004]
    crime_2005_df = crime_df.loc[crime_df['Year'] == 2005]
    crime_2006_df = crime_df.loc[crime_df['Year'] == 2006]
    crime_2007_df = crime_df.loc[crime_df['Year'] == 2007]
    crime_2008_df = crime_df.loc[crime_df['Year'] == 2008]
    crime_2009_df = crime_df.loc[crime_df['Year'] == 2009]
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

    crime_2001 = crime_2001_df.loc[crime_2001_df['Primary Type'] == crime_type]
    count_2001 = int(crime_2001["Primary Type"].count())
    crime_2002 = crime_2002_df.loc[crime_2002_df['Primary Type'] == crime_type]
    count_2002 = int(crime_2002["Primary Type"].count())
    crime_2003 = crime_2003_df.loc[crime_2003_df['Primary Type'] == crime_type]
    count_2003 = int(crime_2003["Primary Type"].count())
    crime_2004 = crime_2004_df.loc[crime_2004_df['Primary Type'] == crime_type]
    count_2004 = int(crime_2004["Primary Type"].count())
    crime_2005 = crime_2005_df.loc[crime_2005_df['Primary Type'] == crime_type]
    count_2005 = int(crime_2005["Primary Type"].count())
    crime_2006 = crime_2006_df.loc[crime_2006_df['Primary Type'] == crime_type]
    count_2006 = int(crime_2006["Primary Type"].count())
    crime_2007 = crime_2007_df.loc[crime_2007_df['Primary Type'] == crime_type]
    count_2007 = int(crime_2007["Primary Type"].count())
    crime_2008 = crime_2008_df.loc[crime_2008_df['Primary Type'] == crime_type]
    count_2008 = int(crime_2008["Primary Type"].count())
    crime_2009 = crime_2009_df.loc[crime_2009_df['Primary Type'] == crime_type]
    count_2009 = int(crime_2009["Primary Type"].count())
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

    
    year = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014',\
            '2015','2016','2017','2018']

    # specify an array crime_count

    crime_count = [count_2001, count_2002, count_2003, count_2004, count_2005, count_2006, count_2007, count_2008, count_2009, \
                   count_2010, count_2011, count_2012, count_2013, count_2014, count_2015, count_2016, count_2017, count_2018]
    
    # define a dataframe using the above

    crime_dict = {'Crime Count':crime_count,'Year':year}

    # convert the above to tuples (zipping the data in the required format)

    mod_result = [{"Crime Count":i, "Year":b} for i, b in zip(crime_dict["Crime Count"], crime_dict["Year"])]

    final_result = json.dumps(mod_result)

    return final_result



############################################################################################################
### Running main function
if __name__ == "__main__":
    app.run(debug=True)
####################################################################################################




