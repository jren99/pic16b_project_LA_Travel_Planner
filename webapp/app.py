from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup as soup
import folium
import import_ipynb
import polyline
import random
import ipynb
import route_functions 
import scraper_functions
from geopy.geocoders import Nominatim


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

dataframe_touristsite = pd.read_csv('2520_touristsite.csv')
dataframe_hotels = pd.read_csv('450_hotel.csv')
list_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

@app.route('/route/', methods=['POST', 'GET'])
def route():
    if request.method == 'GET':
        return render_template('route.html')
    else:
        try:
            want_to_go_name = request.form['site']
            hotel_want_to_go_name = request.form['hotel']
            travel_length = request.form['days']
            return render_template('route.html', name=request.form.keys())
        except:
            return render_template('route.html')


@app.route('/route/<site>/', methods=['POST', 'GET'])
def route_plot(name):
    
    visit_html_tourist = visit_tourist(dataframe_touristsite, want_to_go_name)
    locations = find_location_site(visit_html_tourist)
    hotel_visit_html = visit_hotel(dataframe_hotels, hotel_want_to_go_name)
    hotel_location=find_location_hotel(hotel_visit_html)

    geolocator = Nominatim(user_agent = "pic16b")
    locations = location_cleaner(locations)
    df = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"])
    for location in locations:
        loc = geolocator.geocode(location) # geocoding the location
        df.loc[len(df.index)] = [loc, loc.longitude, loc.latitude]
    
    hotel = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"])
    hotel_locations = location_cleaner(hotel_location)
    for location in hotel_locations:
        loc = geolocator.geocode(location) # geocoding the location
        hotel.loc[len(df.index)] = [loc, loc.longitude, loc.latitude]

    url = "http://router.project-osrm.org/route/v1/car/-118.475712,34.076951;-118.300293,34.118219;-118.361879,34.138321"
    r = requests.get(url) # getting the request
    res = r.json()
    polyline.decode('yj~nEh|brUzG~AeAhH~IwBjL}Tx_@eXag@wIkDoGpFyHzkBo{Ahk@yT{@iGmTyhAuwD{iGu_AcjBy@whHacAJU}kBkd@a@aT_kBqZyI{Xf`@{\\hJlGdJZ|VnG_L|MkAqW}AeGyOz\\iJ`Y{^jZlHpSjkBbNXSxgBc_@~s@cz@rWshAfgAsVj{@qNpQcC}D')

    coordinates = locations_per_day(df, travel_length)

    route_list = []
    for i in range(len(coordinates)):
        test_route = get_route(coordinates[i], hotel)
        route_list.append(test_route)

    maps = []
    for i in range(len(route_list)):
        maps.append(get_map(route_list[i], list_colors[i]))

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