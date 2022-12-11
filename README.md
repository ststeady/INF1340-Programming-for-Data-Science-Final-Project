# Data Analysis on Heart Attack

## Purpose and Description of the Project

Cardiovascular disease has become one of the most common conditions nowadays in the world. As the concerns are rising for the public, this project intends to study a specific symptom, heart attack, in order to determine main causes of it. The projects contains analysis from three different levels, descriptive, diagnostic as well as predictive analysis, and finally draws conclusions from the analysis.

## Main Features

1. The program includes several functions that can help users explore descriptive summary statistics such as mean, maximum, minimum and standard deviation of the various specified variables.
2. The program provides a full diagnostic analysis on top of the aforementioned descriptive summary to highlight key relationships and correlations betweent the variables. 
3. The program also includes a scatterplot that shows the relationship between age and blood pressure using linear regression functions, as well as a visualization of a correlation matrix. 
4. The program also conducts a predictive analysis based on the descriptive and diagnostic data generated, and allows for a more in-depth insight into the correlation and future predictions as a result of these analyses.
5. The program has various API functions that allow for customized outputs based on the users specified parameters of the function arguments.
6. The program also includes the visualization of a ROC curve for logistic regression.

## Execution instructions

All functions are executable using the name provided in the .py file. The variables and variable types are specified in the API file. In addition, numpy, pandas, seaborn, matplotlib and various toolkits from sklearn are required interpreters for analytical functions. 

## Example of Running

```python
# returns an integer number of the individuals within the dataset that have an age of over 56 and a chol of over 251.
print(two_var_diag(df_0, "age",56,"chol",251))

# returns an integer number of the individuals who have a chest pain of type 0 and are classified as less risk of heart attacks.  
print(cp_type(0,"less"))
  
# returns an integer number of the individuals who have a fbs of over 120 ml/dl and are classified as less risk of heart attacks.
print(fbs("over","less"))
```
  
## Data and Sources

This dataset is downloaded from Kaggle from the author RASHIK RAHMAN, the data uploading page is titled <em>Heart Attack Analysis & Prediction Dataset</em>. 

The data contains 14 entities such as age, sex, number of major vessels, resting blood pressure and so on for 304 selected samples, the data is last updated in 2020.
  
The source link on Kaggle is [https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
