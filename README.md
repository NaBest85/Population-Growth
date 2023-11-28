# TITLE OF PROJECT

# UNC Charlotte Data Analytics Bootcamp Final Project

---

## This is the GitHub repository for our Boot Camp group's final project. 

### Group Members: (embed links to everyone’s repository with their names)


<img width="870" alt="Screenshot 2023-11-28 at 12 32 00 AM" src="https://github.com/NaBest85/Population-Growth/assets/135518113/1b5a576d-c131-41f1-906f-cddf36d902b5">




While members are assigned specific roles, we all worked together on each part of the project. 

---

## Selected Topic - Place Holder

Overview:

Objective:

## Questions We Would Like to Answer:

Question 1
Question 2
Question 3
Etc.

#### Locations of Project Deliverables:

<img width="597" alt="Screenshot 2023-11-28 at 12 32 57 AM" src="https://github.com/NaBest85/Population-Growth/assets/135518113/b00f6b4a-bb1d-477e-bb05-87eccfdad2e2">




#### Presentation:
Our presentation is hosted on Google Slides, and can be found here. (Embed link in here)

###### Technologies & Tools Used:
Design a picture with the logos
Technologies: Tableau, PostgreSQL
Languages: Python, HTML, CSS
Tools: Jupyter Notebook
Algorithms: Linear Regression, Correlation Matrix, Forecasting, Statistical, Geographic


###### Data Exploration Phase:
Inset a pic
ETA
Extract, Transform, Load

###### Data Analysis Phase:
Detailed descriptions of our data analysis can be found in our [presentation] (add link).

Insert charts and brief analysis of said charts


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

![Initial 3D PCA](Images/ML_initial.png)

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
Our dashboard can be found [here](add the link), or embedded on this [website](add link) we have created to present our final project.

Png of Dashboard

#### Analysis Results:




#### Recommendations for Future Analysis:



#### Improvements We Would Have Made:





