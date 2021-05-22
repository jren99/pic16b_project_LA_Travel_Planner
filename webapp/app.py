from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup as soup


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')


def visit_tourist(df, want_to_go_name):
    each_name = want_to_go_name.split(".")
    
    for name in each_name:
        if name == each_name[0]:
            visit_html = df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"] == name]
        else:
            visit_html = visit_html.append(df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"] == name])
    
    return visit_html

def find_location(visit_html):
    
    location = []
    
    for link in visit_html["Site Link"]:
        html = requests.get(link)
        bsobj = soup(html.content, "lxml")
    
        for loc in bsobj.find_all("script", type = "application/ld+json"):
            if "streetAddress" in loc.string:
                find_part_html = loc.string.split("{")
                for street in find_part_html:
                    if "streetAddress" in street:
                        for value in street.split(","):
                            if "streetAddress" in value:
                                street_name = value.split(":")[1][1:][:-1] + ", "
                                   
                            if "addressLocality" in value:
                                city_name = value.split(":")[1][1:][:-1] + ", "
                                 
                            if "postalCode" in value:
                                zipcode = "CA " + value.split(":")[1][1:][:-1]
                            
        location_info = street_name + city_name + zipcode
        location.append(location_info)
    
    return location


@app.route('/route/', methods=['POST', 'GET'])
def route():
    if request.method == 'GET':
        return render_template('route.html')
    else:
        try:
            return render_template('route.html', name=request.form['name'])
        except:
            return render_template('route.html')


@app.route('/route/<name>/', methods=['POST', 'GET'])
def route_plot(name):
    visit_html_tourist = visit_tourist(dataframe_touristsite, name)
    location = find_location(visit_html_tourist)
    return render_template('route.html', name=name, location=location)


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

if __name__ == "__main__":
    app.run(debug=True)