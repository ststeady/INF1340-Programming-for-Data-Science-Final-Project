# Data Analysis on Heart Attack

## Purpose and Description of the Project

Cardiovascular disease has become one of the most common conditions nowadays in the world. As the concerns are rising for the public, this project intends to study a specific symptom, heart attack, in order to determine main causes of it. The projects contains analysis from three different levels, descriptive, diagnostic as well as predictive analysis, and finally draws conclusions from the analysis.

## Main Features

1. The program includes several functions that can help users explore summary statistics such as mean, maximum, minimum and standard deviation.
2. The program provides a full report of all the countries' emission analysis, as well as report on country of users' entry. 
3. The program includes barplot which can visualize $CO^2$ emission over years within a conutry
4. The program compares two countries' emission in the same year, as well as two years' emission within the same country
5. The program has customizable functions feature which allows users to get summary statistics of the country and period of their choices.

## Execution instructions

All functions are executable using the name provided in the .py file. The variables and variable types are specified in the API file. In addition, numpy, pandas, seaborn, matplotlib and various toolkits from sklearn are required interpreters for analytical functions. 

## Example of Running

```python
# returns average CO2 emission of Canada between 1990 and 2000
print(getcustavg("Canada", 1990, 2000))

# report every single countries' summary statistics  
reportall()
  
# returns bar plot of Canada's CO2 emission from 1750 to 2017
getcountrybar("Canada")
```
  
## Data and Sources

This dataset is downloaded from Kaggle from the author RASHIK RAHMAN, the data uploading page is titled <em>Heart Attack Analysis & Prediction Dataset<em>. 

The data contains 14 entities such as age, sex, number of major vessels, resting blood pressure and so on for 304 selected samples, the data is last updated in 2020.
  
The source link on Kaggle is [https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
