# pic16b_project

## Travel Planning
1. **Abstract:**


2. **Planned Deliverables:** Concisely what you are going to create and what capabilities it will have. Are you making a webapp? A Python package for others to use? Code that creates a novel data set? Etc. Please consider two scenarios:
We will create a travel recommendation generator that will give hotel and sightseeing recommendations based on where you want to go in California. We will also generate the optimal traveling route to go to each of the different locations. The user will input a city in California that they want to go to, which will generate the sightseeing recommendations, then generate hotel recommendations, and the optimal routes between the sightseeing locations and the hotel location.

	* “Full success.” What will your deliverable be if everything works out for you exactly as you plan?
Our deliverable will be a web app that allows the user to input the city and generates recommendations based on what the user selects. It will then display the optimal routes for traveling between the sightseeing locations and the hotel location.

	* “Partial success.” What useful deliverable will you be able to offer even if things don’t 100% work out? For example, maybe you aren’t able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan!
Partial success will be defined by a web app that only generates the optimal routes provided that the user has already decided on a hotel and some sightseeing locations.

3. **Resources Required:** Do you need certain data sets? Do you know whether those data sets exist? Are they freely accessible? You should do at least a small amount of research for this part, in which you convince me that there is good reason to believe that you will be able to access or obtain the resources needed for your proposal.
TripAdvisor will have the data on the sightseeing locations and the hotel locations, and the google map API will generate the optimal routes.

4. **Tools/Skills Required:** What skills will you need? Machine learning, database management, complex visualization, something else? If you know the names of Python packages that you will need to use, include them here. If you’re not sure, just describe the skills or tasks you will need to accomplish.
Web scraping for both hotel and sightseeing recommendations (scrapy)
geographic visualization for plotting sightseeing recommendations (plotly)
Complex visualizations for generating maps of travelling routes  (google maps API)

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
