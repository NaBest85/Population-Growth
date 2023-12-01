# FORECASTING POPULATION GROWTH AND ECONOMIC IMPACTS: A Comprehensive Analysis of the Best States 2024

# UNC Charlotte Data Analytics Bootcamp Final Project

---

## This is the GitHub repository for our Boot Camp group's final project. 

### Group Members:

![Roles _ Responsibilities-2](https://github.com/NaBest85/Population-Growth/assets/135518113/91d8e7c3-def5-4ead-a017-594c7f088850)

While members are assigned specific roles, we all worked together on each part of the project. 

---

## Selected Topic - Population and Economic Growth

Overview: This project strives to forecast population growth and analyze its economic implications in various U.S. states. Using data sets related to population growth, cost of living, new businesses, and wages, we have developed a machine-learning model and interface to rank the Best States for 2024. Further, we have employed visualization techniques, such as Tableau dashboards, correlation matrices, and linear regression charts, to present our conclusions effectively.

Objective: The direct objective of this project is to deliver insights into the connection between population growth and economic factors in different states. By forecasting population growth and evaluating its impact on economic indicators like cost of living, new business opportunities, and wages, we aim to identify the Best States for 2024. The project's secondary objective is to showcase the results through visualizations, including a Tableau dashboard, correlation matrix, and linear regression charts, to enhance understanding and foster data-driven decision-making.

## Questions We Would Like to Answer:

Question 1: How  were the variables and data sets selected for the machine learning models and Tableeau used to forecast population growth and economic impacts? Essentionally, how is the numeric change in a state's GDP, population, salary, housing costs, unemployment rate, new small businesses and other factors calculated?

Question 2: What insights can be obtained from analyzing the correlation matrix chart and the two linear regression charts in order to understand the relationship between total population and growth, birth/death rates and eeconomic factors in different states?

Question 3: Can someone explain the methodology used to rank the Best States 2024 based on forecasted population growth and economic indicators?

Question 4: What is the distribution of household income across different income brackets? What percentage of households have a total income below $10,000 and above $200,000?

#### Locations of Project Deliverables:

![Objectives](https://github.com/NaBest85/Population-Growth/assets/135518113/e677a23b-2aa1-4396-8226-b0890041cf62)

#### Presentation:
Our presentation is hosted on Google Slides, and can be found [here](https://docs.google.com/presentation/d/e/2PACX-1vQUnxHTNXRGel638romLxZZx8syTqLE9BSV0MyXXXReIcBTcswT9ux-yQugeViF5FIvhif2OMjBK2VV/pub?start=false&loop=true&delayms=10000).

Our machine learning interface is hosted on Python Anywhere, and the model can be found [here](http://rahiembrooks.pythonanywhere.com).

###### Technologies & Tools Used:

![TOOLS EMPLOYED FOR DATA ANALYSIS](https://github.com/NaBest85/Population-Growth/assets/135518113/5c6126e4-c1bf-4d97-b164-f2e3a55acfe0)

###### Data Exploration Phase:

![ETL for DATA EXPLORATION](https://github.com/NaBest85/Population-Growth/assets/135518113/32753b98-9fc0-4c6e-98a4-7f15be3b773e)


###### Data Analysis Phase:
Detailed descriptions of our data analysis can be found in our [presentation](https://docs.google.com/presentation/d/e/2PACX-1vQUnxHTNXRGel638romLxZZx8syTqLE9BSV0MyXXXReIcBTcswT9ux-yQugeViF5FIvhif2OMjBK2VV/pub?start=false&loop=true&delayms=10000).

Here is a chart the shows x, y, z.

<img width="574" alt="SCIKIT_LEARN POPULATION CHANGE LINEAR REGRESSION" src="https://github.com/NaBest85/Population-Growth/assets/135518113/f1407c38-ce92-4831-a54b-aa8c6d784130">

- SUMMARY

###### Data Sources:

List Sources with Links


#### Database:
- For our database, we will be using PostgreSQL by use of pgAdmin. The image below represents the tables of data that are uploaded onto the database in Postgres. 

- The most common and obvious connect between all of our datasets is… (Make an observation)

#### Machine Learning:

###### Preliminary Data Processing:
- The first steps were to check the kind of data types were inside of the CSV file housing our data for each state. We found that our dataset had city name, state, county and other variables, leaving the ranges from 2020-2022. 

- The next was to check for duplicates and null values in the dataframe we created. We chose to keep the first of each of the duplicates and drop all rows that did not have data reflecting US states or our time frame of focus.

In the first week, we were able to complete the initial unsupervised clustering. We attained the following 3D Pricincipal Cluster Analysis Plot from this data.

Photo of testing model

###### Preliminary Feature Engineering, Feature Selection, & Decision-making Process:


###### Splitting Data Into Testing & Training sets:
For our final linear regression model, we used an 80/20 testing/training split to achieve our results. The testing/training splits we tried in other methods are shown in the table below.


###### Explanation of Model Choice (Including Limitations & Benefits):

Here are the models we tried, along with results we got:


The Linear Regression model outperformed the closest model by 40x RMSE. Since it was the most simple solution, we tried a few other models as well to see if we could outperform it.


The second closest was random forest regression 

This model is over 3x more accurate than the other random forest models attempted 

This includes the Gradient BoostingRegressor which is built to optimize validation error, while also stopping training trees before overfitting occurs. 



#### Dashboard:

We used *Tableau* to create and host our dashboard.
- The dashboard for the Popultion Vs Income Heat Maps can be found here: (https://public.tableau.com/app/profile/nicholas.best8688/viz/Population-Income_17012671879200/2020?publish=yes)
- The dashboard for the Birth and Death chart can be found here: https://public.tableau.com/app/profile/ross.branch/viz/BirthsandDeathsTotals/Story1,  
- The dashboard for Population Change can be found here: https://public.tableau.com/app/profile/ross.branch/viz/EstimatedPopulationTotals/Story1- The dashboard for the HouseHole Income can be found here: https://public.tableau.com/app/profile/nicholas.best8688/viz/HouseHoldIncome_17011334138390/Households10kandunder?publish=yes.

Png of Dashboard

#### Analysis Results:




#### Recommendations for Future Analysis:



#### Improvements We Would Have Made:





