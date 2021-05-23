from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup as soup
from geopy.geocoders import Nominatim
import folium
import polyline
import random


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

def visit_hotel(df, want_to_go_name):
    each_name = want_to_go_name.split(".")
    
    for name in each_name:
        if name == each_name[0]:
            visit_html = df[["Hotel Name", "Site Link"]][df["Hotel Name"] == name]
        else:
            visit_html = visit_html.append(df[["Hotel Name", "Site Link"]][df["Hotel Name"] == name])
    
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

def location_cleaner(locations):
    locations_copy = []
    for location in locations:
        location = location.rsplit(' ', 1)[0]
        words = location.split()
        location_length = len(words)
        for i in range(location_length, 0, -1):
            if geolocator.geocode(location) != None:
                locations_copy.append(location)
                break
            location = location.rsplit(' ', 1)[0]
    return locations_copy

def locations_per_day(df, travel_length):
    travel_length = int(travel_length)
    loc_per_day = []
    number_of_locs = df.shape[0]
    while travel_length != 0:
        loc_per_day.append(number_of_locs // travel_length)
        number_of_locs -= (number_of_locs // travel_length)
        travel_length -= 1
    random.shuffle(loc_per_day)
    
    coordinates = [0] * len(loc_per_day)
    used_coordinates = []
    addresses = [0] * len(loc_per_day)
    
    for i in range(len(coordinates)):
        coordinates[i] = []
        addresses[i] = []
        for j in range(0, loc_per_day[i]):
            row = df.sample()
            long_lat = (row.iloc[0]["Longitude"], row.iloc[0]["Latitude"])
            while long_lat in used_coordinates:
                row = df.sample()
                long_lat = (row.iloc[0]["Longitude"], row.iloc[0]["Latitude"])
            coordinates[i].append(long_lat)
            used_coordinates.append(long_lat)
            addresses[i].append(row.iloc[0]["Address"])
            
    return (coordinates, addresses)

def get_route(coordinates, hotel, transportation):
    loc = str(hotel.iloc[0]["Longitude"]) + "," + str(hotel.iloc[0]["Latitude"]) + ";"
    for i in range(len(coordinates)):
        if i == len(coordinates) - 1:
            loc += str(coordinates[i][0]) + "," + str(coordinates[i][1])
        else:
            loc += str(coordinates[i][0]) + "," + str(coordinates[i][1]) + ";"
    
    url = "https://routing.openstreetmap.de/routed-" + transportation + "/route/v1/driving/"
    r = requests.get(url + loc + "?steps=true")
    if r.status_code!= 200:
        print("Failed")
        return {}
  
    res = r.json()   
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][len(res['waypoints']) - 1]['location'][1], res['waypoints'][len(res['waypoints']) - 1]['location'][0]]
    waypoints = []
    for i in range(1, len(res['waypoints']) - 1):
        waypoints.append((res['waypoints'][i]['location'][1], res['waypoints'][i]['location'][0]))
    distance = res['routes'][0]['distance']
    duration = res['routes'][0]['duration']

    out = {'route':routes,
           'start_point':start_point,
           'waypoints': waypoints,
           'end_point':end_point,
           'distance':distance,
           'duration':duration
          } 
    return out

@app.route('/route/', methods=['POST', 'GET'])
def route():
    if request.method == 'GET':
        return render_template('route.html')
    else:
        try:
            return render_template('route.html', site=request.form['site'], day=request.form['day'], hotel=request.form['hotel'], transportation=request.form['transportation'])
        except:
            return render_template('route.html')

geolocator = Nominatim(user_agent = "pic16b")

list_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

def get_map(route, route_color, addresses, hotel_df):
    
    m = folium.Map(location=[(route['start_point'][0] + route['end_point'][0])/2, 
                             (route['start_point'][1] + route['end_point'][1])/2], 
                   zoom_start=15, tooltip = "Hover")

    folium.PolyLine(
        route['route'],
        weight=8,
        color=route_color,
        opacity=0.6
    ).add_to(m)

    folium.Marker(
        location=route['start_point'],
        icon=folium.Icon(icon='play', color='green'),
        popup = hotel_df.iloc[0]["Address"]
    ).add_to(m)

    folium.Marker(
        location=route['end_point'],
        icon=folium.Icon(icon='stop', color='red'),
        popup = addresses[len(addresses) - 1]
    ).add_to(m)
    
    for i in range(len(route['waypoints'])):
        folium.Marker(
            location=route['waypoints'][i],
            icon=folium.Icon(icon='circle', color='blue'),
            popup = addresses[i]
        ).add_to(m)

    return m

@app.route('/route/<site>/<day>/<hotel>/<transportation>/', methods=['POST', 'GET'])
def route_plot(site, day, hotel, transportation):
    visit_html_tourist = visit_tourist(dataframe_touristsite, site)
    location_touristsite = find_location(visit_html_tourist)
    visit_html_hotel = visit_hotel(dataframe_hotel, hotel)
    location_hotel = find_location(visit_html_hotel)
    df = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"])
    locations = location_cleaner(location_touristsite)
    for location in locations:
        loc = geolocator.geocode(location)
        df.loc[len(df.index)] = [loc, loc.longitude, loc.latitude]
    
    hotel_df = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"])
    hotel_locations = location_cleaner(location_hotel)
    for location in hotel_locations:
        loc = geolocator.geocode(location)
        hotel_df.loc[len(df.index)] = [loc, loc.longitude, loc.latitude]
    
    coordinates, addresses = locations_per_day(df, day)

    route_list = []
    for i in range(len(coordinates)):
        test_route = get_route(coordinates[i], hotel_df, transportation)
        route_list.append(test_route)

    maps = []
    for i in range(len(route_list)):
        maps.append(get_map(route_list[i], list_colors[i], addresses[i], hotel_df))

    return render_template('route.html', site=site, hotel=hotel, day=day, transportation=transportation, maps=maps)

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
            return render_template('touristsite.html', name=request.form['names'],headings=touristsite_header, data=touristsite_body)
        except:
            return render_template('touristsite.html',headings=touristsite_header, data=touristsite_body)

@app.route('/touristsite/<name>/', methods=['POST', 'GET'])
def touristsite_name(name):
    touristsite_header = tuple(dataframe_touristsite)
    dataframe_touristsite_update = dataframe_touristsite[dataframe_touristsite["Tourist Site Name"].str.contains(str(name))]
    touristsite_body_update = tuple(dataframe_touristsite_update.itertuples(index=False, name=None))
    return render_template('touristsite.html', name=name, headings_update=touristsite_header, data_update=touristsite_body_update)

dataframe_ht = pd.read_csv('420_hotel.csv')
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