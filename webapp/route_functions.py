import scraper_functions
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup as soup
import folium
import import_ipynb
import polyline
from geopy.geocoders import Nominatim
import random 



# Cleans the addresses by removing the code at the end and then removing the last word of the address with each iteration of
# the loop. OSM sometimes has trouble recognizing addresses that have extra details in the middle of their addresses. 
dataframe_touristsite = pd.read_csv('2520_touristsite.csv')
dataframe_hotels = pd.read_csv('450_hotel.csv')
geolocator = Nominatim(user_agent = "pic16b")

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

 # Determines the number of attractions that the user must visit per day and randomly chooses attractions for each day.
def locations_per_day(df, travel_length):
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

def get_route(coordinates, hotel, transportation=None):
     loc = str(hotel.iloc[0]["Longitude"]) + "," + str(hotel.iloc[0]["Latitude"]) + ";"
     for i in range(len(coordinates)):
         if i == len(coordinates) - 1:
            loc += str(coordinates[i][0]) + "," + str(coordinates[i][1])
         else:
            loc += str(coordinates[i][0]) + "," + str(coordinates[i][1]) + ";"
     # loc += str(hotel.iloc[0]["Longitude"]) + "," + str(hotel.iloc[0]["Latitude"]) # unaable to perform round trip
     url = "http://router.project-osrm.org/route/v1/" + transportation + "/"
     r = requests.get(url + loc) # same thing as what we did before, getting the request
     if r.status_code!= 200: # I don't know what this means
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

     out = {'route':routes,
           'start_point':start_point,
           'waypoints': waypoints,
           'end_point':end_point,
           'distance':distance,
           'duration':duration
          } # returning a dictionary with the routes, starting point, ending point, and distance

     return out

 # Using folium to draw the route on an interactive map. Since none of us are really familiar with folium, it would be worth
# seeing if we can accomplish the same results but using plotly express instead.
def get_map(route, route_color, addresses):
    
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
        popup = dataframe_hotels.iloc[0]["Address"]
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

def route_plot(want_to_go_name, hotel_want_to_go_name, travel_length):
    
    visit_html_tourist = scraper_functions.visit_tourist(dataframe_touristsite, want_to_go_name)
    locations = scraper_functions.find_location_site(visit_html_tourist)
    hotel_visit_html = scraper_functions.visit_hotel(dataframe_hotels, hotel_want_to_go_name)
    hotel_location=scraper_functions.find_location_hotel(hotel_visit_html)

    
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
    list_colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple"
    ]
    maps = []
    for i in range(len(route_list)):
        maps.append(get_map(route_list[i], list_colors[i]))
    return maps

    