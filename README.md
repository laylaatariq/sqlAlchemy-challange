# sqlAlchemy-challange

This project contains two files performing different actions using SQLAlchemy and Flask.

***The first file is purely SQLAlchemy that performs the following functions:***
1. Precipitation Analysis
    1. Get the date an year before from the last data point in the database
    2. Retrieve date and respective precipitation scores
    3. Plot a histogram using the data retrieved before
    4. Calculate Summary Stats for precipitation data and store in into a dataframe
2. Station Analysis
    1. Calculate the total number of stations
    2. Get which station is most active
    3. Get Min, Max, Avg Temp for that station
    4. Get the temperature data of lsat 12 months for this station and create a histogram
    5. Use the function given to get the previous stated stats for a certain time period
    6. Use those results to create a bar chart with error bar
    7. Calculate the total amount of rainfall for each station for the given time period

***The second file creates an api that uses SQLAlchemy, Flask and JSON:***
1. Create different routes
2. Use SQL queries to retrieve data
3. Output the data onto the screen in JSON format
4. Different routes created:
    "/Measurements"
    "//api/v1.0/stations"
    "/api/v1.0/precipitation"
    "/api/v1.0/tobs"
    "/api/v1.0/startDate"
    "/api/v1.0/startDate/endDate"
