# Cleans the addresses by removing the code at the end and then removing the last word of the address with each iteration of
# the loop. OSM sometimes has trouble recognizing addresses that have extra details in the middle of their addresses. 
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

def get_route(coordinates, hotel, transportation):
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
        popup = hotel.iloc[0]["Address"]
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