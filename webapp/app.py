from flask import Flask, render_template, url_for, request, redirect # use for making the webapp
import pandas as pd # use to modify dataframe
import csv # read csv files
import requests # send http requests
from bs4 import BeautifulSoup as soup # use for webscraping locations
from geopy.geocoders import Nominatim # Geopy is a Python client for geocoding. We use the Nominatim geocoder for OpenStreetMap (OSM) data.
import folium # visualizes data on map; wondering if I can replace this with plotly express
import polyline # Python implementation of Google’s Encoded Polyline Algorithm Format
import random
from helper_function import isfloat

app = Flask(__name__)

## trying to add the like feature, currently not working yet
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

# db = SQLAlchemy(app)

# class users(db.Model):
#     '''
#     store places user likes
#     '''
#     _id = db.Column("id", primary_key=True)
#     site = db.Column(db.String(100))
#     site_link = db.Column(db.String(1000))

#     def __init__(self, site, site_link):
#         self.site = site
#         self.site_link = site_link

@app.route('/', methods=['POST', 'GET'])
def main():
    """
    This controls the 'Home' page.
    """
    return render_template('main.html')

# import the csv file after webscraping the recommended tourist sites on TripAdvisor
dataframe_ts = pd.read_csv('2520_touristsite.csv')
# get the data from columns of "Rank", "Tourist Site Name", "Site Link"
dataframe_touristsite = dataframe_ts[["Rank", "Tourist Site Name", "Site Link"]]
# get the headers into a tuple
touristsite_header = tuple(dataframe_touristsite)
# get the data of the dataframe into a tuple
touristsite_body = tuple(dataframe_touristsite.itertuples(index=False, name=None))

@app.route('/touristsite/', methods=['POST', 'GET'])
def touristsite():
    """
    This function controls the 'Tourist Attraction Recommendations' page.
    Get the input of the tourist site keyword by the user.
    """
    if request.method == 'GET':
            return render_template('touristsite.html',headings=touristsite_header, data=touristsite_body)
    else:
        try:
            return render_template('touristsite.html', name=request.form['name'],headings=touristsite_header, data=touristsite_body)
        except:
            return render_template('touristsite.html',headings=touristsite_header, data=touristsite_body)

@app.route('/touristsite/<name>/', methods=['POST', 'GET'])
def touristsite_name(name):
    """
    This function receives the input of the keyword from the above 'touristsite' function
    and returns a filtered dataframe with all the tourist sites containing that input keyword.
    """
    # get the header of the dataframe
    touristsite_header = tuple(dataframe_touristsite)
    # filter the dataframe by not being case-sensitive and not including NaN rows
    dataframe_touristsite_update = dataframe_touristsite[dataframe_touristsite["Tourist Site Name"].str.contains(str(name).lower(), na = False, case = False)]
    # fill up the rows of the dataframe
    touristsite_body_update = tuple(dataframe_touristsite_update.itertuples(index=False, name=None))
    
    return render_template('touristsite.html', name=name, headings_update=touristsite_header, data_update=touristsite_body_update)

# import the csv file after webscraping the recommended hotels on TripAdvisor
dataframe_ht = pd.read_csv('420_hotel.csv')
# add a col 
# new col is the rating of the hotel
dataframe_ht['Rate (out of 5)']=dataframe_ht['Rate'].str.split(" ").str[0].astype(float)
# get the data from columns of "Rank", "Hotel Name", "Rate", "Site Link"
dataframe_hotel = dataframe_ht[["Rank", "Hotel Name", "Rate (out of 5)", "Site Link"]]

# get the headers into a tuple
hotel_header = tuple(dataframe_hotel)
# get the data of the dataframe into a tuple
hotel_body = tuple(dataframe_hotel.itertuples(index=False, name=None))


    

@app.route('/hotel/', methods=['POST', 'GET'])
def hotel():
    """
    This function controls the 'Hotel Recommendations' page.
    Get the input of the hotel keyword by the user.
    """
    if request.method == 'GET':
            return render_template('hotel.html',headings=hotel_header, data=hotel_body)
    else:
        try:
            return render_template('hotel.html', name=request.form['name'],headings=hotel_header, data=hotel_body)
        except:
            return render_template('hotel.html',headings=hotel_header, data=hotel_body)

@app.route('/hotel/<name>/', methods=['POST', 'GET'])
def hotel_name(name):
    """
    This function receives the input of the keyword from the above 'hotel' function
    and returns a filtered dataframe with all the hotels containing that input keyword.
    """
    # get the header of the dataframe
    hotel_header = tuple(dataframe_hotel)
    # filter the dataframe by not being case-sensitive and not including NaN rows
    if isfloat(name):
         # find hotel ratings that are larger than or equal to the input number
        dataframe_hotel_update = dataframe_hotel[dataframe_hotel["Rate (out of 5)"]>=float(name)]
    else:
       # find the hotels which names contain keywords
        dataframe_hotel_update = dataframe_hotel[dataframe_hotel["Hotel Name"].str.contains(str(name).lower(), na = False, case = False)]
    # fill up the rows of the dataframe
    hotel_body_update = tuple(dataframe_hotel_update.itertuples(index=False, name=None))
    
    return render_template('hotel.html', name=name, headings_update=hotel_header, data_update=hotel_body_update)

# import the csv file after webscraping the recommended restaurants on TripAdvisor
dataframe_rt = pd.read_csv('13460_restaurant.csv')
# add a new col for the rating 
dataframe_rt['Rate (out of 5)']=dataframe_rt['Rate'].str.split(" ").str[0].astype(float)
# get the data from columns of "Rank", "Restaurant Name", "Style", "Rate", "Site Link"
dataframe_restaurant = dataframe_rt[["Rank", "Restaurant Name", "Style", "Rate (out of 5)", "Site Link"]]
# get the headers into a tuple
restaurant_header = tuple(dataframe_restaurant)
# get the data of the dataframe into a tuple
restaurant_body = tuple(dataframe_restaurant.itertuples(index=False, name=None))

@app.route('/restaurant/', methods=['POST', 'GET'])
def restaurant():
    """
    This function controls the 'Restaurants Recommendations' page.
    Get the input of the restaurant keyword by the user.
    """
    if request.method == 'GET':
            return render_template('restaurant.html',headings=restaurant_header, data=restaurant_body)
    else:
        try:
            return render_template('restaurant.html', name=request.form['name'],headings=restaurant_header, data=restaurant_body)
        except:
            return render_template('restaurant.html',headings=restaurant_header, data=restaurant_body)

@app.route('/restaurant/<name>/', methods=['POST', 'GET'])
def restaurant_name(name):
    """
    This function receives the input of the keyword from the above 'restaurant_name' function
    and returns a filtered dataframe with all the restaurants containing that input keyword.
    """
    # get the header of the dataframe
    restaurant_header = tuple(dataframe_restaurant)
    if isfloat(name):
        # filter dataframe with rating higher than or equal to the input
        dataframe_restaurant_update = dataframe_restaurant[dataframe_restaurant["Rate (out of 5)"]>=float(name)]
    else:
        # filter the dataframe by not being case-sensitive and not including NaN rows
        dataframe_restaurant_update = dataframe_restaurant[dataframe_restaurant["Style"].str.contains(str(name).lower(), na = False, case = False)]
    # fill up the rows of the dataframe
    restaurant_body_update = tuple(dataframe_restaurant_update.itertuples(index=False, name=None))
    
    return render_template('restaurant.html', name=name, headings_update=restaurant_header, data_update=restaurant_body_update)

def visit_tourist(df, want_to_go_name):
    """
    Get the site links based on the input of the tourist sites the user wants to go.
    """
    # lowercase the input
    want_to_go_name = want_to_go_name.lower()
    # split the string to separate each name of the tourist sites
    each_name = want_to_go_name.split(", ")
    
    for name in each_name:
        if name == each_name[0]:
            visit_html = df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"].str.lower() == name]
        else:
            visit_html = visit_html.append(df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"].str.lower() == name])
    
    return visit_html

def visit_hotel(df, want_to_go_name):
    """
    Get the site links based on the input of the hotel the user wants to go.
    """
    
    visit_html = df[["Hotel Name", "Site Link"]][df["Hotel Name"].str.lower() == want_to_go_name.lower()]
    
    return visit_html
    
def find_location(visit_html):
    """
    Get the information of the locations by webscraping through the site links.
    """
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
    """
    Cleans the addresses by removing the code at the end 
    and then removing the last word of the address with each iteration of the loop.
    """
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
    """
    Determines the number of attractions that the user must visit per day 
    and randomly chooses attractions for each day.
    """
    travel_length = int(travel_length)
    loc_per_day = []
    number_of_locs = df.shape[0]
    while travel_length != 0:
        loc_per_day.append(number_of_locs // travel_length)
        number_of_locs -= (number_of_locs // travel_length)
        travel_length -= 1
    random.shuffle(loc_per_day) # obtain a random ordering of locations per day
    
    coordinates = [0] * len(loc_per_day)
    used_coordinates = []
    addresses = [0] * len(loc_per_day)

    # creates nested lists of tuples within a list that indicate the coordinates of the places you visit per day
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
    routes = polyline.decode(res['routes'][0]['geometry']) # the geometry specifies the polyline encoding
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]] # 0th waypoint corresponds to the starting location
    end_point = [res['waypoints'][len(res['waypoints']) - 1]['location'][1], res['waypoints'][len(res['waypoints']) - 1]['location'][0]] # len - 1 waypoint corresponds to the ending location
    waypoints = []
    for i in range(1, len(res['waypoints']) - 1):
        waypoints.append((res['waypoints'][i]['location'][1], res['waypoints'][i]['location'][0]))
    distance = res['routes'][0]['distance']
    duration = res['routes'][0]['duration']

    # returning a dictionary with the routes, starting point, ending point, and distance
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
    """
    This function controls the 'Plan Your Trip!' page.
    Get the input of the tourist sites, number of days planning to stay in LA, 
    hotel, and the type of transportation by the user.
    """
    if request.method == 'GET':
        return render_template('route.html')
    else:
        try:
            return render_template('route.html', site=request.form['site'], day=request.form['day'], hotel=request.form['hotel'], transportation=request.form['transportation'])
        except:
            return render_template('route.html')

geolocator = Nominatim(user_agent = "pic16b")

# list of colors for plotting different routes
list_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

def get_map(route, route_color, addresses, hotel_df):
    """
    Draw the route on an interactive map.
    """
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
    """
    This function receives the inputs from the above 'route' function
    and returns several links to generate the route for each day.
    """
    visit_html_tourist = visit_tourist(dataframe_touristsite, site)
    location_touristsite = find_location(visit_html_tourist)
    visit_html_hotel = visit_hotel(dataframe_hotel, hotel)
    location_hotel = find_location(visit_html_hotel)
    # creating the Pandas dataframe
    df = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"])
    locations = location_cleaner(location_touristsite)
    for location in locations:
        loc = geolocator.geocode(location) # geocoding the location
        df.loc[len(df.index)] = [loc, loc.longitude, loc.latitude] # adding the location, longitude, and latitude to the dataframe
    
    hotel_df = pd.DataFrame(columns = ["Address", "Longitude", "Latitude"]) # creating the Pandas dataframe
    hotel_locations = location_cleaner(location_hotel)
    for location in hotel_locations:
        loc = geolocator.geocode(location) # geocoding the location
        hotel_df.loc[len(df.index)] = [loc, loc.longitude, loc.latitude] # adding the location, longitude, and latitude to the dataframe
    
    coordinates, addresses = locations_per_day(df, day)

    # obtain the list of routes for the entire travel
    route_list = []
    for i in range(len(coordinates)):
        test_route = get_route(coordinates[i], hotel_df, transportation)
        route_list.append(test_route)

    maps = []
    for i in range(len(route_list)):
        maps.append(get_map(route_list[i], list_colors[i], addresses[i], hotel_df))
    
    for i in range(0, len(maps)):
        maps[i].save("templates/map"+str(i)+".html")

    # for i in range(0, len(maps)):
    #     print("Day {}".format(i+1))
    #     print("The traveling distance is {} m".format(route_list[i]["distance"]) )
    #     print("The traveling duration is {} min".format(route_list[i]["duration"]/60))

    return render_template('route.html', site=site, hotel=hotel, day=day, transportation=transportation, maps=maps)

@app.route('/map1/')
def route_map1():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    
    return render_template('map0.html')

@app.route('/map2/')
def route_map2():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map1.html')

@app.route('/map3/')
def route_map3():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map2.html')

@app.route('/map4/')
def route_map4():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map3.html')

@app.route('/map5/')
def route_map5():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map4.html')

@app.route('/map6/')
def route_map6():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map5.html')

@app.route('/map7/')
def route_map7():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map6.html')

@app.route('/map8/')
def route_map8():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map7.html')

@app.route('/map9/')
def route_map9():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map8.html')

@app.route('/map10/')
def route_map10():
    """
    This function returns a webpage showing a route map, which is shown on the 'Plan Your Trip!' page.
    """
    return render_template('map9.html')

@app.route('/contact/')
def contact():
    """
    This function controls the 'Contact Us' page.
    """
    return render_template('contact.html')

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)