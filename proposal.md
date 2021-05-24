# PIC16b Project
**Group Members:**

Ashley Lu

Jaya Ren

Jingxuan Zhang

## Travel Planning
1. **Abstract:**
When it comes to traveling, sometimes it can be a struggle to plan out where you want to go, especially if you're going somewhere you've never been to before. Our project aims to create a travel planning tool that gives sightseeing and hotel recommendations based on which city the user wants to go to, and also visualizes the optimal routes between the sightseeing locations and hotel locations. To accomplish this, we will use web scraping to obtain the recommended locations for a given city, use geographic visualizations to see all of the different locations on a map, and use the Google Maps API to figure out what are the optimal routes between all of the places the user wants to go to.

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

6. **Ethics:**
Depending on what recommendations Tripadvisor gives us, maybe the sightseeing locations will privilege some cultural sites above others, depending on what races and ethnicities are more prevalent in a location. Also, if we’re recommending sightseeing and hotel locations, Tripadvisor might favor larger and more popular sites rather than smaller sites. As popularity is largely based on positive reviews, it's hardly objective since there are many bogus positive reviews.

7. **Tentative Timeline:** 
- After two weeks: We want to be able to fetch a list of sightseeing places based on the input city. To achieve this, we might need to build a database by scraping data from some sources first, and then learn how to fetch relevent data, possibly using sql.
- After four weeks: We want to learn how to work with API to generate recommended routes for traveling, and maybe generate a list of hotel recommendations. For the hotel recommendations, it can be a possible machine learning project.
- After six weeks: We want to set up a webapp that allows user to enter a city and then returns places, routes, and hotels recommendations.
