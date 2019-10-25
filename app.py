from flask import Flask, render_template, request, jsonify
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

    if request.method == 'POST':
        #plot = form.plot.data
        crime = form.crime.data
        print('crime=', form.crime.data, " len=", len(crime))
        print('plot=', form.plot.data)
        return 'ok done test'
        #return '<h1>State: {}, City: {}</h1>'.format(form.crime.data, plot)

    return render_template('main.html', form=form)
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
