### DST-and-traffic-implications ###
**By Curtis Hope Hill, Jeffrey Floyd, and Mary Schindler**
A study into the effects of daylight savings on traffic incidents in the city of Chicago, IL

[Link to Kaggle](https://smoosavi.org/datasets/us_accidents), from where the data was obtained.


## Table of Contents ##
[Link to Executive Summary](https://docs.google.com/document/d/1ocNE4wLrWzBJRzkGMlQuR9KBSb5BC2hwFOq3vOTioyU/edit?usp=sharing)

- Assignment Requirements
- Problem Statement
- Background
- Data Cleaning and EDA
- Modeling
- Hypothesis Testing
- Streamlit App
- Recommencations & Conclusions
- Limitations & Future Considerations


## From Assignment: Requirements ##
**For the purposes of a DSI project, we met a few technical requirements. They are:**

1. A README.md file in your project repo. Note that README files are automatically rendered by GitHub when you view a repo. Your README should contain:
    - A problem statement.
    - A succinct formulation of the question your analysis seeks to answer.
    - A table of contents, which should indicate which notebook or scripts a stakeholder should start with, and a link to an executive summary.
    - A paragraph description of the data you used, plus your data acquisition, ingestion, and cleaning steps.
    - A short description of software requirements (e.g., Pandas, Scikit-learn) required by your analysis.

2. Your notebook(s) should be reproducible and error-free. This means:
    - You should set a random seed at the start of every notebook. This will ensure that the random numbers generated in your notebook will be the same every time.
    - You need to provide a relative path to your data, so that if I clone your repo to my machine I can run everything in your repo without error. (You also provide links to any publicly accessible data.)
    - I should be able to Restart & Run All in your notebook(s) and see that the exact same results are reproduced.
    - To check that everything worked properly, you may consider forking your own repo to a different location on your computer and checking that all notebooks can run properly from top to bottom.

3. Bear in mind that the value you provide may come from data ingestion, data cleaning, EDA, and/ or a dashboard, etc. While a model may not be immediately apparent, be creative. Without us telling you exactly what model to build, how could you build a model to increase performance or generate better insights when answering the problem you are facing?


## Problem Statement
We have been contracted by a rideshare company to look into the impacts of the spring and fall Daylight Savings Time changes on traffic accidents. To accomplish this we will be using Sobhan Moosavi’s US Accidents dataset that has gathered ~ 1.5 million US traffic accidents from February 2016 to December of 2020. The goal of this project will be to develop a model that can predict the severity (on a 1-4 scale) of a given traffic accident, and then deploy that model for use in real-time. 


## Background
Daylight Savings Time (DST) is an annual time change that occurs in the spring and fall in nearly seventy (70) countries across the globe. In the United States the time change to DST begins annually at 2:00 AM on the second Sunday in March. DST ends at 2:00 AM on the first Sunday in November. Numerous studies have been done attempting to correlate the change to DST and negative health and behavioral impacts.


### Data Cleaning and EDA ###
The original dataset contained 1,516,064 accident entries from 2016 to 2020, ranking the traffic impact of each accident on a scale of 1 to 4. Due to computing power the dataset was paired down to for different datasets, each representing the geographical area surrounding: Chicago, Boston, Atlanta, and Denver.

A function called 'mrclean' was responsbility for cleaning the each cities' data. Once the data was cleaned and various features extracted from 'datetime' types (year, month, week, etc.), a feature 'IS_DST' was generated based on weather or not the accident took place the week following the change to DST.


### Modeling ###


### Hypothesis Testing ###


### Streamlit App ###


### Recommendations & Conclusions ###
While we found that the end of Daylight Savings in the Fall has no statistically relevant effect on average severity of traffic impact, the start of Daylight Savings in the Spring has a large effect on the average severity of traffic impact in all cities we observed

Because the impact is so significant at the start of Daylight Savings Sigmoids Data Science can confidently recommend that Rideshare Company ® begin lobbying to abolish Daylight Savings altogether. 


### Limitations & Future Considerations ###