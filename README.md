# PIC16b Project
Group Members:
Ashley Lu
Jaya Ren
Jingxuan Zhang

## Travel Planning
1. **Abstract:**


2. **Planned Deliverables:** Concisely what you are going to create and what capabilities it will have. Are you making a webapp? A Python package for others to use? Code that creates a novel data set? Etc. Please consider two scenarios:
We will create a travel recommendation generator that will give hotel and sightseeing recommendations based on where you want to go in California. We will also generate the optimal traveling route to go to each of the different locations. The user will input a city in California that they want to go to, which will generate the sightseeing recommendations, then generate hotel recommendations, and the optimal routes between the sightseeing locations and the hotel location.

	* “Full success.” What will your deliverable be if everything works out for you exactly as you plan?
Our deliverable will be a web app that allows the user to input the city and generates recommendations based on what the user selects. It will then display the optimal routes for traveling between the sightseeing locations and the hotel location.

	* “Partial success.” What useful deliverable will you be able to offer even if things don’t 100% work out? For example, maybe you aren’t able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan!
Partial success will be defined by a web app that only generates the optimal routes provided that the user has already decided on a hotel and some sightseeing locations.

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

7. **Tentative Timeline:** 
- After two weeks: We want to be able to fetch a list of sightseeing places based on the input city. To achieve this, we might need to build a database by scraping data from some sources first, and then learn how to fetch relevent data, possibly using sql.
- After four weeks: We want to learn how to work with API to generate recommended routes for traveling, and maybe generate a list of hotel recommendations. For the hotel recommendations, it can be a possible machine learning project. 
- After six weeks: We want to set up a webapp that allows user to enter a city and then returns places, routes, and hotels recommendations.