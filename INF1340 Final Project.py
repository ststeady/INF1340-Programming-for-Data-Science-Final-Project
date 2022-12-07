#Michael Jiang 1003799703
#INF1340H Programming for Data Science
#Maher Elshakankiri
#Master of Information
#Faculty of Information
#University of Toronto


#Final Project: Group 13
#The following program outputs descriptive and diagnostic analysis of a csv dataset.
#Date Created: Dec/3/2022
#Date Last Modified: Dec/3/2022

#Variables: Age, Cholesterol, Resting BP, Chest Pain Type, Output

#Import necessary tools
import pandas as pd
import numpy as np

#Open dataset file & create dataframe
file = pd.read_csv("heart.csv")

df = file.drop(["sex","trtbps","restecg","thalachh","exng","oldpeak","slp","caa","thall"], axis=1)

print("The following dataframe shows the selected variables that will be used for this area of analysis:")
print(df,"\n","\n")

#Descriptive Analysis:
print("DESCRIPTIVE ANALYSIS")
print("\n","The descriptive analysis for the chosen variables are as follows:")
print(df.describe(),"\n")

#Create new dataframes based on risk of heart attack (0 or 1)
output_0 = df['output']==0
df_0 = df[output_0]
print("Output 0: Less risk of heart attack","\n",df_0,"\n")

output_1 = df['output']==1
df_1 = df[output_1]

print("Output 1: Higher risk of heart attack","\n",df_1,"\n")

#1) Age - Output

print("\n", "1) AGE")
print("The average age of those labeled as less risk of heart attack is:",int(df_0["age"].mean()))
print("The max age of those labeled as less risk of heart attack is:",int(df_0["age"].max()))
print("The min age of those labeled as less risk of heart attack is:",int(df_0["age"].min()),"\n")

print("On the other hand:")
print("The average age of those labeled as higher risk of heart attack is:",int(df_1["age"].mean()))
print("The max age of those labeled as higher risk of heart attack is:",int(df_1["age"].max()))
print("The min age of those labeled as higher risk of heart attack is:",int(df_1["age"].min()),"\n")

print("Therefore, there is no conclusive evidence to show a direct correlation between higher age and a increased impact on risk of heart attacks.")

#2) Cholesterol - Output
print("\n", "2) CHOLESTEROL")

print("The average cholesterol of those labeled as less risk of heart attack is:",int(df_0["chol"].mean()))
print("The max cholesterol of those labeled as less risk of heart attack is:",int(df_0["chol"].max()))
print("The min cholesterol of those labeled as less risk of heart attack is:",int(df_0["chol"].min()),"\n")

print("On the other hand:")
print("The average cholesterol of those who are labeled as higher risk of heart attack is:",int(df_1["chol"].mean()))
print("The max cholesterol of those who are labeled as higher risk of heart attack is:",int(df_1["chol"].max()))
print("The min cholesterol of those who are labeled as higher risk of heart attack is:",int(df_1["chol"].min()),"\n")

print("Therefore, there is also no conclusive evidence to show a direct correlation between higher cholesterol and a increased impact on risk of heart attacks.")

#3) Fasting Blood Sugar - Output
print("\n", "3) FASTING BLOOD SUGAR")
count = len(df_0[df_0["fbs"]==1])

def fbs(fbs_level,risk):
    if fbs_level == "over" and risk == "less":
        count = len(df_0[df_0["fbs"]==1])
        return(count)
    elif fbs_level == "under" and risk == "less":
        count = len(df_0[df_0["fbs"]==0])
        return(count)
    elif fbs_level == "over" and risk == "higher":
        count = len(df_1[df_1["fbs"]==1])
        return(count)
    elif fbs_level == "under" and risk == "higher":
        count = len(df_1[df_1["fbs"]==0])
        return(count)
    
print("Num. of individuals w/ fbs over 120 mg/dl labeled as less risk of heart attack is:", fbs("over","less"))
print("Num. of individuals w/ fbs over 120 mg/dl labeled as higher risk of heart attack is:",fbs("over","higher"),"\n")

print("On the other hand:")
print("Num. of individuals w/ fbs under 120 mg/dl labeled as less risk of heart attack is:",fbs("under","less"))
print("Num. of individuals w/ fbs under 120 mg/dl labeled as higher risk of heart attack is:",fbs("under","higher"),"\n")

print("Here, we can see a slight correlation between individuals with a fbs under 120 mg/dl and a increased risk of heart attacks.")

#4) Chest Pain Type - Output
print("\n", "4) CHEST PAIN TYPE")

def cp_type(cp_type,risk):
    if cp_type == 0 and risk == "less":
        count = len(df_0[df_0["cp"]==0])
        return(count)
    elif cp_type == 1 and risk == "less":
        count = len(df_0[df_0["cp"]==1])
        return(count)
    elif cp_type == 2 and risk == "less":
        count = len(df_0[df_0["cp"]==2])
        return(count)
    elif cp_type == 3 and risk == "less":
        count = len(df_0[df_0["cp"]==3])
        return(count)
    elif cp_type == 0 and risk == "higher":
        count = len(df_1[df_1["cp"]==0])
        return(count)
    elif cp_type == 1 and risk == "higher":
        count = len(df_1[df_1["cp"]==2])
        return(count)
    elif cp_type == 2 and risk == "higher":
        count = len(df_1[df_1["cp"]==3])
        return(count)
    elif cp_type == 3 and risk == "higher":
        count = len(df_1[df_1["cp"]==4])
        return(count)
    
print("Num. of individuals w/ cp type 0 (typical angina) labeled as less risk of heart attack is:", cp_type(0,"less"))
print("Num. of individuals w/ cp type 0 (typical angina) labeled as higher risk of heart attack is:", cp_type(0,"higher"),"\n")

print("Num. of individuals w/ cp type 1 (atypical angina) labeled as less risk of heart attack is:", cp_type(1,"less"))
print("Num. of individuals w/ cp type 1 (atypical angina) labeled as higher risk of heart attack is:", cp_type(1,"higher"),"\n")

print("Num. of individuals w/ cp type 2 (non-anginal pain) labeled as less risk of heart attack is:", cp_type(2,"less"))
print("Num. of individuals w/ cp type 2 (non-anginal pain) labeled as higher risk of heart attack is:", cp_type(2,"higher"),"\n")

print("Num. of individuals w/ cp type 3 (asymptomatic) labeled as less risk of heart attack is:",cp_type(3,"less"))
print("Num. of individuals w/ cp type 3 (asymptomatic) labeled as higher risk of heart attack is:", cp_type(3,"higher"),"\n")

print("Here, we can see a correlation between individuals with atypical angina (type 1 cp) and a higher risk of heart attack.","\n","\n")

#Diagnostic: Relations betweens variables (Work in progress)
print("DIAGNOSTIC ANALYSIS")
print("\n","The diagnostic analysis for the chosen variables are as follows:","\n")

def two_var_diag(output_df,var1,value1,var2,value2):
    for i in df_0.index:
        if df_0[(df_0[str(var1)] > int(value1)) & (df_0[str(var2)] > int(value2))]:
            count = len(output_df[output_df["output"]==1])
            return(count)
        
    
    

#1) Age & Chol above avg, return number of higher risk counts
    #if age > 56(avg) and chol > 251, return number of higher and lesser risk counts
print(two_var_diag(df_0,"age",56,"chol",251))

#2) Age & fbs above avg, return number of higher risk counts
    #if age > 56(avg) and fbs = 1, return number of higher and lesser risk counts 


#3) Age & chest pain type above avg, return number of higher risk counts
    #if age > 56(avg) and cp = 1, return number of higher and lesser risk counts




    
