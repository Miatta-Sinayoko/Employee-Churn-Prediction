# <a name="top"></a>Employee_Attrition_Prediction_Project
![]()


***
[[Project Problem](#project_problem]
[[Project Description](#project_description)]
[[Project Goal](#planning)]
[[Project Plan](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

## <a name="project_problem"></a>Project Problem:
[[Back to top](#top)]

Employee turnover, commonly referred to as "employee Attrition," poses a substantial financial burden on companies. Replacing an employee entails significant costs, as evidenced by a study conducted by the Center for American Progress. According to their findings, companies typically expend approximately one-fifth of an employee's salary to secure a replacement, and this cost escalates significantly when replacing executives or high-earning personnel. In essence, the financial impact of employee turnover remains noteworthy for most employers.

The expenses associated with employee replacement stem from various factors. The process involves considerable time and effort invested in interviewing and selecting a suitable candidate. Moreover, sign-on bonuses and other incentives further contribute to the overall cost. Additionally, the transition period for the new employee to adapt to their new role leads to a decline in productivity for several months, further exacerbating the financial implications.

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

This machine learning classification  project objective is to produce an accurate ML  model that can identify key factors of employee churn at IBM. The project will use data from the IEEE Xplore Digital Library on IBM HR ANALYTICS EMPLOYEE ATTRITION & PERFORMANCE to explore the drivers of employee churn and to identify three employee features and likelyhood of churn. The project will be presented to head of /human Resources and IBM stakeholders, expound on featuren effecacy performance in our machine learning model and the impacts to IBM.


***
## <a name="project_goal"></a>Project Goal: 
[[Back to top](#top)]


-  Identify Drivers of Attrition: Determine the features within the dataset that exhibit strong correlations with employee attrition.
- Build Predictive Model: Develop a high-performing model that can identify Attrition based on the selected features.
- Share Insights: Communicate the findings and model insights to IBM Human resources executives for further analysis and decision-making.

### Initial Questions

1. Is there a relationship between Age and employee Attrition?
2. Is there a relationship between Eudcation and employee Attrition?
3. Is there a relationship between Tenure (Years at Company(IBM)) and employee Attrition

### Target 

The target variable in this dataset is Attrition, which indicates whether an employee has left the company. The value of Attrition is 1 if the employee has left the company and 0 if the employee has not left the company.

### Initial Hypotheses

Hypothesis 1

alpha = .05
**$H_{0}$**: Age  is independent of employee Attrition
**$H_{a}$**: Age is dependent on employee Attrition
Outcome: We will accept or reject the Null Hypothesis.

Hypothesis 2

alpha = .05
**$H_{0}$**: Eudcation is independent of employee  Attrition
**$H_{a}$**: Eudcation is dependent on employee  Attrition
Outcome: We will accept or reject the Null Hypothesis.

Hypothesis 3

alpha = .05
**$H_{0}$**: Tenure  is independent of employee  Attrition
**$H_{a}$**: Tenure  is dependent on employee  Attrition
Outcome: We will accept or reject the Null Hypothesis.




## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Dictionary

The IBM employee attrition dataset is a mixed metric dataset that contains information about 1,470 IBM employees and 35 indivisual features and whether they have left the company (churn). The dataset can be used to explore the factors that contribute to employee attrition and to build predictive models that can be used to predict which employees are at risk of leaving the company.



### Data Dictionary

| Column Name   | Data Type | Description                                              | Possible Values                                      |
|---------------|-----------|----------------------------------------------------------|------------------------------------------------------|
| Age           | int64     | Represents the age of the employee.                      | Integer values                                       |
| Tenure        | int64     | Represents the number of years an employee has worked at the company. Originally "YearsAtCompany". | Integer values                                       |
| Yes_Attrition | int64     | Indicates whether an employee has left the company. 1 for 'Yes' and 0 for 'No'. Originally "Attrition". | 1 (Yes), 0 (No)                                      |
| Education     | int64     | Represents the educational qualification of the employee. | 1 (High School), 2 (Some College), 3 (Bachelor's Degree), 4 (Masters Degree), 5 (Doctoral Degree) |

**Detailed Column Descriptions:**

- **Age**: 
    - **Description**: The age of the employee.
    - **Data Type**: Integer (int64).
    - **Remarks**: Can be used to evaluate if age is a significant factor in attrition.

- **Tenure**:
    - **Description**: Represents the duration in years that an employee has been with the company.
    - **Data Type**: Integer (int64).
    - **Remarks**: A crucial variable to see if the length of employment correlates with attrition. Originally referred to as "YearsAtCompany" in the dataset.

- **Yes_Attrition**:
    - **Description**: Boolean indicator of if an employee has left the company. 1 denotes that the employee left, and 0 denotes they stayed.
    - **Data Type**: Integer (int64).
    - **Remarks**: This is the target variable for prediction. It was derived from the "Attrition" column, where "Yes" was mapped to 1, and "No" was mapped to 0.

- **Education**:
    - **Description**: Denotes the educational background of the employee.
    - **Data Type**: Integer (int64).
    - **Remarks**: The education level can be decoded as:
        - 1: High School
        - 2: Some College
        - 3: Bachelor's Degree
        - 4: Masters Degree
        - 5: Doctoral Degree





## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Planning

-  Identify the problem to be investigated, such as the impact to IBM.
-  Obtain the required data from the the csv created.
-  Create a cREADME.md file documenting all necessary information.
[[Back to top](#top)]

![]()


## <a name="acquire"></a>Data Acquisition and Preparation:
[[Back to top](#top)]

![]()

- Acquire data from  file_path turned csv via (https://ieee-dataport.org/documents/ibm-hr-analytics-employee-attrition-performance)
- The data set has 35 columns and 1,470 rows ,each row represents individual employee numerical data and each column is attributes of the employees
- Clean and prepare the data. This includes removing missing values, correcting errors, and formatting the data in a way that is easy to analyze.Drop unnecessary axis, renaming of featurs, find nulls ,drop nulls, check preperation
 
### Wrangle steps: 
- dropped duplicate rows.
- created dummies for certain features
- created function to acquire and prep data
- function created to prep data 
- renamed Yearsatwork column to 'Tenure'



## <a name="explore"></a>Exploratory Analysis:
[[Back to top](#top)]

-  Python files used for exploration:
    - explore.py
    - wrangle.py
- Exploratory data analysis (EDA) notebook was created utilize visualizations visualizations and statistical tests to explore the data and identify patterns and relationships of the data set.Statistical test utilized are CHI 2 and Pearson correlation.
- Split dataset and acquire baseline



## <a name="model"></a>Modeling:
[[Back to top](#top)]

- Employ advanced training techniques to optimize model learning and performance.
- Selecting a machine learning algorithm and training a model to predict employee Attrition.
- Evaluation will be conducted via variety of models such as Random forrest, logistic regression and  Decision Tree model to determine how well it predicts employee Attrition.
- Implement modeling inconjunction wit Libtaries
- Train the model 
- Implement rigorous validation methods to evaluate the model's ability to generalize and its reliability.
- Opt for the highest-performing model, like Logistic Regression, based on comprehensive evaluation metrics.




## <a name="product"></a>Product Delivery:
[[Back to top](#top)]

- Compile a final notebook that melds top-tier visualizations, well-honed models, and relevant data, offering a robust understanding and conclusions rooted in scientific rigor.
- Produce a `Prediction.csv` file, capturing the chosen model's predictions on test data for subsequent assessment and application.
- Uphold stringent project documentation standards, rooted in both scientific and professional best practices, ensuring an effective presentation or streamlined deployment.

--- 

Deployment. This involves deploying the model in a production environment so that it can be used to predict employee Attrition in real time.




### Reproduce Project

- Install necessary python packages.
- Clone the Employee_Churn_Predicton repo
- Download files from https://ieee-dataport.org/documents/ibm-hr-analytics-employee-attrition-performance
- Unzip and store the csv files in the wine_clustering_project folder.
- Ensure the wrangle.py, explore.py and model.py files are in the same folder as Employee_Attrition_Prediction_Project notebook.ipynb




*********************

## Key Findings 

- **Age:** The graph shows that employee attrition is highest for employees in their 20s and 30s, and then declines as employees get older. This suggests that age may be a factor in employee attrition. Employees in their 20s and 30s may be more likely to leave the company because they are still exploring their career options and they may be more likely to be offered new opportunities at other companies.

-  **Education level:** The chart reveals that there is a significant relationship between education level and employee attrition. The higher the education level, the higher the attrition rate. For example, the attrition rate for employees with a doctoral degree is 25%, while the attrition rate for employees with a high school diploma is only 10%.


-  **Tenure:** The graph shows that employee attrition is highest for employees with less tenure. For example, 15% of employees with less than 1 year of tenure have left the company, while only 5% of employees with more than 10 years of tenure have left the company.


#### Overall, the charts suggest that there are a number of factors that can contribute to employee attrition. Companies can keep their employees by understanding these factors and taking steps to address them.

### Baseline
    
- Baseline Results: 

The baseline accuracy is: 83.22%


    
#### Model 1: Randomn Forest

training score: 89.00%
validate score: 84.01%
Random forest scores are both higher than baseline accuracy

#### Model 2: Logistic Regression

logistic regression training score: 83.22%
logistic regression validate score: 82.99%
Logistic regression scores are both higher than baseline accuracy


#### Model 3: Decision Tree
Decision tree training score: 84.24%
Decision tree validate score: 84.69%
Decision tree scores are both higher than baseline accuracy


## Top Model:

####  Decision Tree


## Testing the Model

- Model Testing Results
Decision tree test score: 88.78%
Train & Validate decision tree model scores were higher than baseline accuracy with a consistant accuracy of 84%. Test Decesion Tree apprx 89%



***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]


## CONCLUSION 

- Three features  selected based on their visual significance and chi-square statistical testing for training the Classification Model to determine their significant relationship .
- Age Hypothesis - We reject the Null Hypothesis, Age is dependent on employee Attrition.
- Education Hypothesis- We reject the Null Hypothesis, education is dependent on  on employee Attrition.
- Tenure Hypothesis - We fail to reject the Null Hypothesis, Tenure is independent of employee Attrition. 
- **Statistical test**- Chi2 and Pearsons R were conducted: 
- Age Hypothesis - We reject the Null Hypothesis, Age is dependent on employee Attrition.
- Education Hypothesis We reject the Null Hypothesis, education is dependent on  on employee Attrition.
- Tenure Hypothesis - We fail to reject the Null Hypothesis, Tenure is independent of employee Attrition.
- **Modeling**:Decision Tree, Logistic Regression, and Random Forest models were implemented with a Random Seed of 123 to avoid overfitting.

- Logistic Regression failed to out perform the baseline accuracy of 83%,the scores were tied in the training and in validation failed to out perform the baseline. Decision Tree had better consistentcy and Random Forest had better accuracy ,both model sets achieved an accuracy of around 84%. The Decision Tree model was chosen for it's consistency.




## RECOMMENDATIONS

1. To keep employees in their 20s and 30s, companies can offer them opportunities for career development and advancement. They can also create a culture that values employee learning and growth.

2.  To keep employees with higher education levels, companies can offer them competitive salaries and benefits. They can also create a culture that values intellectual curiosity and innovation.

3. To keep employees with less tenure, companies can offer them mentorship and training programs. They can also create a culture that values employee engagement and belonging.


# Improving these factors can reduce churn rates.

Here are some additional recommendations:

Offer competitive salaries and benefits: This is one of the most important factors in keeping employees. Employees need to feel that they are being fairly compensated for their work.
Create a positive work environment: This includes factors such as a supportive culture, good relationships with managers, and opportunities for growth.
Provide opportunities for professional development: This shows employees that the company is invested in their careers. It also gives them the skills they need to advance in their careers.
Listen to employee feedback: This shows employees that their voices are heard and that their concerns are taken seriously. It also helps companies identify areas where they can improve.
By following these recommendations, companies can reduce employee attrition and keep their best employees engaged and productive.



## LINKEDIN DESCRIPTION

A ML classification prediction model was was conducted , utilizing IBM Employee Attrition Prediction & Analysis dataset, which contains 1,470 rows and 35 columns To process and visualize the data effectively. The downloaded file_path was then converted into a csv that I will utilize API's to load into the CODEUP database. I Imported the necesary Python libraries explore my data set.
For my modeling I selected the Decision Tree model, which is consistent and typically beats the base line. The primary goal of the project was to identify employee features that led to Attrition with an acurate  ML model . The goal of this data is to contribute to decion making effort for IBM's head of human resources abd stakeholders. 



***
## <a name="sources"></a>Sources:
[[Back to top](#top)]


#### 1.  Carter, A. (2023). Classification Project. GitHub. Retrieved from https://github.com/annie-carter/classification_project
#### 
#### 2.  @data{2m1g-6v47-23,
doi = {10.21227/2m1g-6v47},
url = {https://dx.doi.org/10.21227/2m1g-6v47},author = {M S, Ajmal and DESHPANDE, TANMAY and Data Scientists, IBM},publisher = {IEEE Dataport},title = {IBM HR Analytics Employee Attrition & Performance},year = {2023} }
#### 


### Licensing: Creative Commons Attribution






[[Back to top](#top)]
