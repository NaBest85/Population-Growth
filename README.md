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

The line chart demonstrates the predicted population change for the years 2020-2022 across all 50 states, Washington, DC, and Puerto Rico. The x-axis represents the time period, ranging from 0 to 10, indicating the progression of time. The y-axis represents the magnitude of the population change, ranging from -1.0 to 1.5.

<img width="574" alt="SCIKIT_LEARN POPULATION CHANGE LINEAR REGRESSION" src="https://github.com/NaBest85/Population-Growth/assets/135518113/f1407c38-ce92-4831-a54b-aa8c6d784130">

## Summary
The predicted values in the chart indicate the projected population change for each year. These values are generated using a machine learning model, specifically from the scikit-learn library in Python. The predicted values for each year are as follows:

- For the year 2020, the predicted population change is 0.3789.
- For the year 2021, the predicted population change is 0.4299.
- For the year 2022, the predicted population change is 0.0658.
- And so on...

On the other hand, the true values represent the actual population change observed during the same time period. These values are the ground truth against which the predictions are compared. The true values for each year are as follows:

- For the year 2020, the actual population change is 0.5603.
- For the year 2021, the actual population change is 0.8643.
- For the year 2022, the actual population change is 0.3473.
- And so on...

By comparing the predicted values with the true values, we can evaluate the accuracy of the predictions. This analysis helps in understanding the performance of the machine learning model and its ability to forecast population changes.

###### Data Sources:

[Pandas](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)

[Machine Learner](https://machinelearningmastery.com/how-to-prepare-categorical-data-for-deep-learning-in-python/)  &  [Scikit-Learn](https://machinelearningmastery.com/how-to-prepare-categorical-data-for-deep-learning-in-python/)

[Root Mean Square](https://statisticsbyjim.com/regression/root-mean-square-error-rmse/#:~:text=By%20considering%20the%20scale%20of,error%20rate%20of%20only%204%25.)

#### Database:
The ERD diagram illustrates the interrelationships among state population, employment rate, and unemployment rate. The State entity serves as the primary key across all three tables, facilitating seamless integration between them.

The one-to-one relationships can be succinctly summarized as follows:
  - Each state is uniquely represented by a record in the 'Total State Population' table, and vice versa.
  - Likewise, each state is associated with a single record in the 'State Employment Rate' table, and vice versa.
  - Similarly, each state is linked to a solitary record in the 'Employment Average Salary' table, and vice versa.
  - Additionally, each state has a connected record in the 'Small Business' table, and vice versa.

These one-to-one relationships guarantee the presence of a distinct record for each state in every relevant table. By leveraging the primary key of the 'State' entity, these connections are established and upheld, ensuring a cohesive and comprehensive representation of the data.

![ERD Diagram](https://github.com/NaBest85/Population-Growth/assets/135518113/af32a919-50ab-4d3d-94c4-f2d808e59dc3)

#### Machine Learning:

###### Preliminary Data Processing:
-This dataset is a combination of multiple datasets that have been cleaned and merged for analysis. The cleaning process involved removing duplicates, handling missing values, and standardizing the column names. To eliminate duplicate entries, we used a unique identifier column. For handling missing values, appropriate methods such as imputation with median, mean, or forward-fill were applied. Column names were standardized to ensure consistency across the datasets.

-The merging process involved combining relevant columns from different datasets and different years, ranging from 2020 to 2022. Common identifiers were used to merge the datasets, ensuring accurate and meaningful combinations. By merging the datasets, we aim to gain a broader view of the data and facilitate comprehensive analysis.

-This cleaned and merged dataset will be utilized for various analysis tasks, including but not limited to feature engineering, model training, and evaluation. It provides a consolidated and reliable source of data for conducting in-depth analysis and generating valuable insights.

<img width="799" alt="MERGED CLEANED DATA" src="https://github.com/NaBest85/Population-Growth/assets/135518113/81cd680a-ea64-4f48-8e87-aab58304bda0">

Explanation of Model Choice

<img width="483" alt="LINEAR REGRESSION MODEL" src="https://github.com/NaBest85/Population-Growth/assets/135518113/a8eff9d2-8e28-4561-931a-416a62d4f629">

Here are the linear regression results of our machine learning model:

###### Splitting Data Into Testing & Training sets:
For our final linear regression model, we used an 80/20 testing/training split. This means that 80% of the data was used for training the model, while the remaining 20% was used for testing and evaluating its performance.

###### Explanation of Model Choice (Including Limitations & Benefits):

We experimented with several models and obtained the following results:

The Linear Regression model significantly outperformed the closest model by 40 times in terms of RMSE (Root Mean Squared Error). Due to its simplicity, we also explored other models to assess if any could surpass its performance.

The second closest model in terms of accuracy was the Random Forest Regression model. It displayed over 3 times higher accuracy compared to the other Random Forest models attempted. This includes the Gradient Boosting Regressor, which was designed to optimize validation error and prevent overfitting by stopping tree training at the right point.

#### Analysis Results:

Based on our analysis of the data, we found the following insights:

1. Mean Absolute Error (MAE):
   - The MAE value of 0.04841392466037104 indicates that, on average, the predicted rankings of the Best US States deviate by approximately 0.0484 from the actual rankings. A lower MAE suggests a better fit of the model's predictions to the actual data.

2. Mean Squared Error (MSE):
   - The MSE value of 0.003399581613349438 represents the average squared difference between the predicted and actual rankings. It provides a measure of the overall model's accuracy. The lower the MSE, the better the model's predictions align with the actual rankings.

3. Root Mean Squared Error (RMSE):
   - The RMSE value of 0.05830593120214648 is the square root of the MSE. It measures the average magnitude of the prediction errors. Like MAE and MSE, a lower RMSE indicates a better fit of the model.

Moving on to the coefficients:

1. Job Market Demand:
   - The coefficient of 0.060648 suggests that a higher job market demand positively affects the state's ranking. This means that states with stronger job markets tend to have higher rankings.

2. Cost of Living Index:
   - The coefficient of -0.069957 indicates that a higher cost of living index has a negative impact on the state's ranking. States with lower costs of living tend to rank higher.

3. Industry Growth:
   - The coefficient of 0.497142 suggests that higher industry growth positively influences the state's ranking. States with thriving industries are more likely to have higher rankings.

Finally, the intercept value of 0.451994486667233 represents the baseline ranking value when all factors are zero. It indicates the starting point for the ranking model.

These insights help understand the factors influencing the rankings and their relative importance. States with strong job markets, lower costs of living, and significant industry growth tend to have higher rankings.

#### Recommendations for Future Analysis:

To enhance future analysis, consider the following recommendations:

1. Explore additional variables: Incorporate more factors that might influence state rankings, such as education quality, healthcare access, or crime rates.
2. Include interaction terms: Investigate potential interactions between the existing variables to capture complex relationships that may affect rankings.
3. Expand dataset: Collect more comprehensive data encompassing a wider range of states and time periods to obtain a more representative and robust analysis.

#### Improvements We Would Have Made:

Although our analysis yielded valuable insights, there are areas where improvements could be made:

1. Data quality: Ensure the accuracy and completeness of the data used for analysis, as any gaps or errors could impact the reliability of the results.
2. Model evaluation: Perform a thorough evaluation of various models to identify the most suitable approach, considering different algorithms and techniques beyond the ones explored in this analysis.
3. Feature engineering: Explore additional feature engineering techniques, such as scaling, transforming, or combining variables to enhance the predictive power of the model.

By addressing these aspects, future analyses can yield even more accurate and informative results.
