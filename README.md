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
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
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
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
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



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo_name/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)




2. **Planned Deliverables:** Concisely what you are going to create and what capabilities it will have. Are you making a webapp? A Python package for others to use? Code that creates a novel data set? Etc.
- Description: We will create a travel recommendation generator that will give hotel and sightseeing recommendations based on which city you want to go to. We will also generate the optimal traveling route to go to each of the different locations. The user will input a city in any country that they want to go to, which will generate the sightseeing recommendations, then generate hotel recommendations, and the optimal routes between the sightseeing locations and the hotel location. Potentially we might also implement a way to give a time estimate for how long the user's ideal travel plan is and how long they should stay in the city they chose, though this is not the main focus of our project and we will only implement this provided we have enough time.

- Full success: Ideally, our deliverable will be a web app that allows the user to input a city in any country and generates recommendations based on what the user selects. It will then display the optimal routes for traveling between the sightseeing locations and the hotel location. This would be considered our "full success" product.

- Partial success: Since our group is experimenting with modules and APIs outside the scope of the class, it may be difficult to achieve full success.
In the case that we are not able to accomplish all of our goals, "partial success" will be defined by an optimal route generator framework that shows the optimal routes between the sightseeing locations and hotel locations in a given city in California, obtained from web scraping. In this case, we will not have a webapp that allows the user to input their selections. Rather, choosing the city and sightseeing/hotel locations will be predetermined by our code. Also, by limiting our searching to California, we can work with a smaller scope in case we have difficulties using the Google Maps API, which will be our primary tool in generating the optimal routes.

3. **Resources Required:**
- [TripAdvisor](https://www.tripadvisor.com/): Since our project aims to provide a list of recommended hotels and sightseeing locations after the user inputs the city they want to visit, we need reliable and latest data sets about the sightseeing locations and hotel in that city. Hence, we plan to use the information about hotel locations and sightseeing locations from TripAdvisor. Since there will be a lot of information about the locations, we decide to minimize the options of cities that the user can input. In other words, the user can only input a city in California. We might enlarge the city options in different states for the user in the later stage of the project. The method of how we will get the information from TripAdvisor will mainly be web scraping.
- [Kaggle](https://www.kaggle.com/): If we are not able to successfully get the information from TripAdvisor by web scraping, using the available data sets about the hotel and sightseeing directly online, such as Kaggle, is another option.
- [Google Maps API](https://developers.google.com/maps): Since we need to also provide the optimal route for the user, we have searched online that Google Maps API can be a tool to form maps and routes.

4. **Tools/Skills Required:**
- Web scraping: We need to have information by web scraping TripAdvisor to provide both the hotel and sightseeing recommendations for the user. We have searched online that there are many available tutorials about how to use web scraping to get information from TripAdvisor that we can self-learning them.
- Python Plotly Package (& Pandas Package): It will be better if we will also be able to generate geographic visualizations for plotting sightseeing recommendations based on the information by web scraping from TripAdvisor.
- Google Maps API: We may use complex visualizations for generating maps of traveling routes by Google Maps API. There are also tutorials online about how to use it that we may need to self-learn. We might need to learn how to find the optimal route based on the locations that the user wants to go. If we want manually design the optimal route, we might need to also provide options for the user to select, such as whether the user has a car. These options will be very important, which will decide whether the optimal route is reasonable and workable in reality instead of being an ideal route.
- Webapp skills: We will try to learn how to make our ideas shown on a webapp in the later stage of our project. There are also tutorials online about how to make a webapp.

5. **Risks:**
 - Data:　Important data component might not exist or for technical reasons, it’s really hard to scrape. We plan to scrape informations such as popular tourist spots and hotels from TripAdvisor, but we might not be able to achieve it based on our limited experience with web scraping, or we managed to scrape, but they exist on two sources that we can’t merge.
 - API: We also don’t have experience using APIs so it might end up being too difficult to learn how to use an API by ourselves.
 - Webapp: We don't have previous experience building an webapp, so the final product might not come out as a webapp.

6. **Ethics:**
Depending on what recommendations Tripadvisor gives us, maybe the sightseeing locations will privilege some cultural sites above others, depending on what races and ethnicities are more prevalent in a location. Also, if we’re recommending sightseeing and hotel locations, Tripadvisor might favor larger and more popular sites rather than smaller sites. As popularity is largely based on positive reviews, it's hardly objective since there are many bogus positive reviews.

