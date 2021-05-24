# PIC16b Project
**Contributers:**

Ashley Lu

Jaya Ren

Jingxuan Zhang

## LA Travel planner
<img src="Logo.png" alt="logo" width=30%/>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Ethics">Ethics</a></li>
    <li><a href="#Limitations">Limitations</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="Home.png" alt="home" width=70%/>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Ethics">Ethics</a></li>
    <li><a href="#Limitations">Limitations</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

When it comes to traveling, sometimes it can be a struggle to plan out where you want to go, especially if you're going somewhere you've never been to before. Our project aims to create a travel planning tool that gives attraction, hotel, and food recommendations to LA tourists, and provides a detailed and personalized travel plan based on users' selections, including attractions to go for each day and a route recommendation.


### Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):
Beautiful Soup is a commonly used Python Library by programmers for webscraping. We use Beautiful Soup to get the data, which are saved in CSV files, through webscraping.
* [Geopy](https://geopy.readthedocs.io/en/stable/#nominatim):
Geopy is a Python client for geocoding that obtains the longitude/latitude coordinates for an address. We make use of Nominatim from Geopy, which is a geocoder for OpenStreetMap (OSM), an open data map of the world.
* [OSRM](http://project-osrm.org/docs/v5.24.0/api/#):
OSRM is a routing engine that uses OpenStreetMap (OSM) data to generate the shortest routes between locations. By sending a request to OSRM, you obtain a Polyline encoding that contains information such as the route, distance, and duration.
* [Polyline](https://polyline.readthedocs.io/en/v1.1/):
We use the Python implementation of Polyline, which is Google's Encoded Polyline Algorithm Format that stores a series of coordinates as an encoded string.
* [Folium](http://python-visualization.github.io/folium/):
We use Folium to visualize route data on an interactive leaflet map. Folium supports Polyline, so it is the best module to use with OSRM.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/):
We used Flask to develop our webapp for this project. Since it's written in Python, it makes it easier for us to directly use the functions we have created in Jupyter Notebook and call them after typing the created functions in the webapp files.



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jren99/pic16b_project.git
   ```
2. Install packages
   ```sh
   pip install pandas
   pip install Flask
   pip install beautifulsoup4
   pip install geopy
   pip install folium
   pip install polyline

   ```
### Execution
```sh
   cd webapp
   python3 app.py
   ```



<!-- USAGE EXAMPLES -->
## Usage
After the users open the webapp locally on their computers, the users can see **six clickable buttons** on the top of the webapp:
* **Home**: This page mainly consists of an introduction, such as the purpose and the basic structure, of the webapp.
* **Tourist Attraction Recommendations**: This is the start of the users' journey in LA. Users can see a data list of all the recommended tourist attractions that we got the data through webscraping on TripAdvisor. After the users input a keyword in the search box and click **Search**, the users may see another **two clickable buttons**. The users may click **Click here to see all the possible tourist sites** to see a filtered data list that all the tourist sites contain that keyword will be shown in the list. If the users want to try again to input another keyword, the users may click **Try a new keyword**.
* **Hotel Recommendations**: The users are also able to check the hotels in LA. Similarly, the users can see a list of all the recommended hotels in LA, and we also provided the search box for the users to only see the hotels containing the input keyword by the users.
* **Restaurant Recommendations**: After the users entering this webpage, the users will be able to see a data list containing all the recommended foods in LA. The users can also filter the data list based on their input keyword, such as entering Japanese to search for all the restaurants that provided Japanese foods.
* **Plan Your Trip!**: Based on the recommended tourist attraction list and the recommended hotel list, the users are required to give four inputs, which are several tourist attractions they are interested in, the number of days they plan to stay, one hotel they plan to stay, and the mode of transportation they are going to use. After the users click **Search for an optimized route**, there will be several steps that the users need to follow:
	* **Step One: Click here to generate route.**: The users need to click this button first. Our webapp will automatically go webscraping the locations of the places the users want to go and generate the route. This might take a few seconds based on the number of places the users want to go.
	* **Step Two: Click here to see the Day-n route.** (where n depends on the number of days the users' input): After the webpage has finished loading, the users may click this button to see each day's route we generated for them.
	* **Plan a new trip: Click here.**: This button is for users to enter different inputs and start over the process of generating routes again.
* **Contact Us**: We are welcomed for any suggestions from our users. The users may tell us their suggestions by submitting a Google Form on this webpage.

<!-- ETHICS -->
## Ethics

Depending on what recommendations Tripadvisor gives us, maybe the sightseeing locations will privilege some cultural sites above others, depending on what races and ethnicities are more prevalent in a location. Also, if we’re recommending sightseeing and hotel locations, Tripadvisor might favor larger and more popular sites rather than smaller sites. As popularity is largely based on positive reviews, it's hardly objective since there are many bogus positive reviews.

<!-- LIMITATIONS -->
## Limitations

* Because of the inefficiency of scraper, we were only able to obtain a dataset for LA instead of California or even larger range. Hence, our webapp is limited to users who want to plan a trip to LA. However, we believe a more efficient scraping method can potentially extend the functionality of our app to larger area.
* As our recommendations for hotels, food, and attractions are based on matching keywords, this could lead to certain inaccuracy. For example, Getty Center is a museum but doesn't contain the word "museum" in its name, so it won't be included as one of the search results. Smarter search method or better dataset will be needed for further improvement.
* This planner can only plan up to 10 days.
* Generating the most optimal travel plan such that the user can choose some arbitrary number of attractions and days to stay in LA would be a very difficult problem. To determine the distance/duration of each possible route, we would have to send multiple requests to OSRM, which would be time-consuming and inefficient. We could also treat this as a Traveling Salesman type of problem, but it's unrealistic to construct such a route that passes through all the attractions and find nearby hotels for each of them. We think it makes more sense to have one hotel that the user stays in and use it as the starting point for each day's route. It might also be realistic to add an option for two hotels as well, though our implementation currently does not support this.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [TripAdvisor](https://www.tripadvisor.com/): Since our project aims to provide a list of hotels, attractions, and restaurants recommendations, we need reliable and latest data sets. Hence, we accessed the information above from TripAdvisor. 
* [OpenStreetMap](https://www.openstreetmap.org/copyright): OSM provides all of the map data we use to generate the routes and create the route visualizations. We are very thankful that such an amazing service is open-source!
* []()
