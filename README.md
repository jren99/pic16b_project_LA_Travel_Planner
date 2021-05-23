# PIC16b Project
**Contributers:**

Ashley Lu

Jaya Ren

Jingxuan Zhang

## LA Travel planner

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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

When it comes to traveling, sometimes it can be a struggle to plan out where you want to go, especially if you're going somewhere you've never been to before. Our project aims to create a travel planning tool that gives attraction, hotel, and food recommendations to LA tourists, and provides a detailed and personalized travel plan based on users' selections, including attractions to go for each day and a route recommendation. 


### Built With

* []()
* []()
* [Flask](https://flask.palletsprojects.com/en/2.0.x/):
We used Flask to develop our webapp for this project. Since it's written in Python, it makes it easier for us to call the scraper and route generator we have created. 



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





<!-- ETHICS -->
## Ethics

Depending on what recommendations Tripadvisor gives us, maybe the sightseeing locations will privilege some cultural sites above others, depending on what races and ethnicities are more prevalent in a location. Also, if we’re recommending sightseeing and hotel locations, Tripadvisor might favor larger and more popular sites rather than smaller sites. As popularity is largely based on positive reviews, it's hardly objective since there are many bogus positive reviews.

<!-- LIMITATIONS -->
## Limitations

* Because of the inefficiency of scraper, we were only able to obtain a dataset for LA instead of California or even larger range. Hence, our webapp is limited to users who want to plan a trip to LA. However, we believe a more efficient scraping method can potentially extend the functionality of our app to larger area. 
* 

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [TripAdvisor](https://www.tripadvisor.com/):Since our project aims to provide a list of hotels, attractions, and restaurants recommendations, we need reliable and latest data sets. Hence, we accessed the information above from TripAdvisor.
* []()
* []()







