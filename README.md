## DST-and-traffic-implications
**By Curtis Hope Hill, Jeffrey Floyd, and Mary Schindler**
A study into the effects of daylight savings on traffic incidents in the city of Chicago, IL

[Link to Kaggle](https://smoosavi.org/datasets/us_accidents), from where the data was obtained.


### Table of Contents
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


### From Assignment: Requirements
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


### Problem Statement
We have been contracted by a rideshare company to look into the impacts of the Spring and Fall Daylight Savings Time changes on traffic accidents. To accomplish this we will be using Sobhan Moosavi’s US Accidents dataset that has gathered ~ 1.5 million US traffic accidents from February 2016 to December of 2020. The goal of this project will be to develop a model that can predict the severity (on a 1-4 scale) of a given traffic accident, and then deploy that model for use in real-time. 


### Background
Daylight Savings Time (DST) is an annual time change that occurs in the Spring and Fall in nearly seventy (70) countries across the globe. In the United States the time change to DST begins annually at 2:00 AM on the second Sunday in March. DST ends at 2:00 AM on the first Sunday in November. Numerous studies have been done attempting to correlate the change to DST and negative health and behavioral impacts.


### Data Cleaning and EDA
The original dataset contained 1,516,064 accident entries from 2016 to 2020, ranking the traffic impact of each accident on a scale of 1 to 4. Due to computing power the dataset was paired down to for different datasets, each representing the geographical area surrounding: Chicago, Boston, Atlanta, and Denver.

A function called 'mrclean' was responsbility for cleaning the each cities' data. Once the data was cleaned and various features extracted from 'datetime' types (year, month, week, etc.), a feature 'IS_DST' was generated based on weather or not the accident took place the week following the change to DST.


### Modeling
We wanted to look at the feature importance of the is_DST feature to determine how impactful Daylight Savings could be when predicting accident severity. We focused in on the Chicago data for modeling purposes since it was the largest data set among the cities we observed. 

We tried a few different model types to see which produced the best results: 
- Decision Tree
- Random Forest
- BAG
- XGBoost


### Hypothesis Testing
We also explored ANOVA to make a determination of the statisitcal significance of accident severity during DST. 

For the Spring DST time change:
- H0: There is not a statistically significant difference in the average severity of accidents in Chicago in the weeks before, during, and after the Spring time change.
- Ha: There is a statistically significant difference in the average severity of accidents in Chicago in the weeks before, during, and after the Spring time change.

And similarly for Fall. 

* To test our research hypotheses we ran both an ANOVA and a Kruskal-Wallis(KW) test on accident severity for the spring and fall time changes in Chicago. 
* There were no significant results for the fall time change in Chicago, however there were statistically significant differences for the Atlanta dataset and the combined dataset.
    * In the combined dataset the differences were such that we saw a decrease in accident severity from the week before the fall change to the week of the change.
* The results of the tests for the spring time change showed strong evidence for statistical significance in both the ANOVA(f = 8.69, p-value=0.0002) and KW(statistic=16.61, p-value=0.0002) as both have p-values below our alpha set at 0.05.
* Given this we can reject our null hypothesis for the spring time change and state that there is a statistically significant difference in the average severity of accidents in Chicago during the weeks before, during, and after the spring time change.
* In addition to the ANOVA and KW we also calculated the Eta squared effect size, finding that the effect of the difference we found was of a small size at eta = 0.008.
* We also ran a multiple comparison test to investigate which weeks were different from each other finding:
    * The week before DST and the week of DST were significantly different, with a higher mean severity in the week before DST.
    * and the week of DST and the week after DST were significantly different, with higher mean severity in the week after DST.
* The Chicago results are somewhat counter to what might be expected, however this could be due to the differences in overall accidents for each week. The week of DST had 200 more accidents than the week after DST and almost 400 more than the week before. The higher number of accidents could be lowering the impact of the most severe accidents leading to the lower overall mean of accident severity for the week of DST.



### Streamlit App
We created an Streamlit App that will accept GPS coordinates of a reported accident. It will then get the current local weather data and make a prediction on how severely the accident will impact traffic. The app was based on an XGBoost model. 


### Recommendations & Conclusions
While we found that the end of DST in the Fall has no statistically relevant effect on average severity of traffic impact, the start of DST in the Spring has a large effect on the average severity of traffic impact in all cities we observed

Because the impact is so significant at the start of DST Sigmoids Data Science can confidently recommend that Rideshare Company ® begin lobbying to abolish DST altogether. 


### Limitations & Future Considerations
1. Limitations
    - Individual computing power prevented processing of full data set
    - Accidents of severity 1 seem to be either underreported or misreported. This potentially limited our ability to model this label as accurately as other labels.
    - Individual cities see impacts at different rates making it more difficult to paint a broader picture of DST impact
    - Dependency incompatibility for certain Python packages that could increase streamlit user-friendliness
    
2. Future Considerations
    - NLP on the dropped feature “description”  to see if a determination could be made on accident locations. For example, a service road can be beneath a highway and accidents could happen in both locations but it’s more likely for an accident to occur at higher speeds on the highway. 
    - Further ANOVA to include the frequency of accidents and impact of Day/Night on accident severity during the week of DST.
    - Additional modeling on cities other than Chicago to see if the models’ performance holds across geographic locations.
    - Contact the creator of the dataset and ask what the quality of “accident severity” measures (how long the duration of each severity is).
    - Integrate GeoPandas into the Streamlit app in order to have ‘drag-and-drop’ functionality with the map. 

