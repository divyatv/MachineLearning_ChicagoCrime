from flask import Flask, render_template, request, jsonify
from flask import send_file
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret'
'''
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crime = db.Column(db.String(2))
    name = db.Column(db.String(50))
'''
class Form(FlaskForm):
    crime = SelectField('crime', choices=[('ba', 'battery'), ('bu','burglary'), \
                ('da','damage'), ('n','narcotics'), ('o','other'), ('t', 'theft', )]) 
    plot = SelectField('plot', choices=[('pl','plain'), ('he','hexbin'),  \
                                    ('sb', 'seaborn-box'), ('sp','seaborn-pair')])

@app.route('/', methods=['GET', 'POST'])
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
'''
@app.route('/plot/<crime>')
def plot(crime):
    cities = City.query.filter_by(crime=crime).all()

    plotArray = []

    for plot in cities:
        plotObj = {}
        plotObj['id'] = plot.id
        plotObj['name'] = plot.name
        plotArray.append(plotObj)

    return jsonify({'cities' : plotArray})
'''

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port= 5001)
