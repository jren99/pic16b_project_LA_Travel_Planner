from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup as soup

app = Flask(__name__)
'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('main.html', tasks=tasks)
'''

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')

@app.route('/route/', methods=['POST', 'GET'])
def route():
    if request.method == 'GET':
        return render_template('route.html')
    else:
        try:
            return render_template('route.html', name=request.form['name'])
        except:
            return render_template('route.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

dataframe_ts = pd.read_csv('2520_touristsite.csv')
dataframe_touristsite = dataframe_ts[["Rank", "Tourist Site Name", "Site Link"]]
touristsite_header = tuple(dataframe_touristsite)
touristsite_body = tuple(dataframe_touristsite.itertuples(index=False, name=None))

@app.route('/touristsite/', methods=['POST', 'GET'])
def touristsite():
    if request.method == 'GET':
            return render_template('touristsite.html',headings=touristsite_header, data=touristsite_body)
    else:
        try:
            return render_template('touristsite.html', name=request.form['name'],headings=touristsite_header, data=touristsite_body)
        except:
            return render_template('touristsite.html',headings=touristsite_header, data=touristsite_body)

@app.route('/touristsite/<name>/', methods=['POST', 'GET'])
def touristsite_name(name):
    touristsite_header = tuple(dataframe_touristsite)
    dataframe_touristsite_update = dataframe_touristsite[dataframe_touristsite["Tourist Site Name"].str.contains(str(name))]
    touristsite_body_update = tuple(dataframe_touristsite_update.itertuples(index=False, name=None))
    return render_template('touristsite.html', name=name, headings_update=touristsite_header, data_update=touristsite_body_update)

dataframe_ht = pd.read_csv('419_hotel.csv')
dataframe_hotel = dataframe_ht[["Rank", "Hotel Name", "Rate", "Site Link"]]
hotel_header = tuple(dataframe_hotel)
hotel_body = tuple(dataframe_hotel.itertuples(index=False, name=None))

@app.route('/hotel/', methods=['POST', 'GET'])
def hotel():
    if request.method == 'GET':
            return render_template('hotel.html',headings=hotel_header, data=hotel_body)
    else:
        try:
            return render_template('hotel.html', name=request.form['name'],headings=hotel_header, data=hotel_body)
        except:
            return render_template('hotel.html',headings=hotel_header, data=hotel_body)

@app.route('/hotel/<name>/', methods=['POST', 'GET'])
def hotel_name(name):
    hotel_header = tuple(dataframe_hotel)
    dataframe_hotel_update = dataframe_hotel[dataframe_hotel["Hotel Name"].str.contains(str(name))]
    hotel_body_update = tuple(dataframe_hotel_update.itertuples(index=False, name=None))
    return render_template('hotel.html', name=name, headings_update=hotel_header, data_update=hotel_body_update)

dataframe_rt = pd.read_csv('13460_restaurant.csv')
dataframe_restaurant = dataframe_rt[["Rank", "Restaurant Name", "Style", "Rate", "Site Link"]]
restaurant_header = tuple(dataframe_restaurant)
restaurant_body = tuple(dataframe_restaurant.itertuples(index=False, name=None))

@app.route('/restaurant/', methods=['POST', 'GET'])
def restaurant():
    if request.method == 'GET':
            return render_template('restaurant.html',headings=restaurant_header, data=restaurant_body)
    else:
        try:
            return render_template('restaurant.html', name=request.form['name'],headings=restaurant_header, data=restaurant_body)
        except:
            return render_template('restaurant.html',headings=restaurant_header, data=restaurant_body)

@app.route('/restaurant/<name>/', methods=['POST', 'GET'])
def restaurant_name(name):
    dataframe_restaurant_drop = dataframe_restaurant.dropna()
    restaurant_header = tuple(dataframe_restaurant_drop)
    dataframe_restaurant_update = dataframe_restaurant_drop[dataframe_restaurant_drop["Style"].str.contains(str(name))]
    restaurant_body_update = tuple(dataframe_restaurant_update.itertuples(index=False, name=None))
    return render_template('restaurant.html', name=name, headings_update=restaurant_header, data_update=restaurant_body_update)

'''
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)
'''

if __name__ == "__main__":
    app.run(debug=True)