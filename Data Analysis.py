import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Group A studying variables: age,cp,trtbps,chol,output
# Group B studying variables: sex,exang,thalach,oldpeak,output
# Sub-groups study may not be limited to the above variables...

df = pd.read_csv("heart.csv")
print(df.head())

# print out the correlation matrix and deciding which variables to study
corr_matrix = df.corr()
print(corr_matrix)

# visualizing the correlation matrix
mask = np.triu(np.ones_like(corr_matrix,dtype=bool))
sns.heatmap(corr_matrix,cmap="BuPu",annot=True,mask=mask)

# visualizing the variables distribution
color = '#9A32CD'
df.hist(bins=15,figsize=(25,15),color=color)
plt.rcParams['font.size'] = 20

# Group A: numerical variables and categorical variables
num_var = ["age","trtbps","chol"]
cat_var = ["cp","slp","output"]

# Group A: splitting shape printing function
def gp_A_num_splitshape(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)
    print("The training set X has shape"+ str(X_train.shape)+ "\n"+\
           "The testing set X has shape" + str(X_test.shape) + "\n"+\
           "The training set y has shape" + str(y_train.shape) + "\n"+\
           "The testing set y has shape" + str(y_test.shape)+ "\n")

# Group A: predicted value and expected value function
def gp_A_num_regression(X_train,X_test,y_train,y_test):
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train,y=y_train)
    predicted = linear_regression.predict(X_test)
    expected = y_test
    for i, j in zip(predicted[::5], expected[::5]):
        print(f'predicted:{i:2f}, expected:{j:.2f}')
    print("\n")


def gp_A_num_prediction(age,X_train,y_train):
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    predict = (lambda i: linear_regression.coef_ * i + linear_regression.intercept_)
    print("The predicted value at age " + str(age) + " is " + str(predict(age)))


# Group A: scatterplot of final prediction accuracy function
def gp_A_num_scat(exp,res,X_train,y_train):
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    predict = (lambda i: linear_regression.coef_ * i + linear_regression.intercept_)
    plt.figure(figsize=(8, 4.5))
    sns.scatterplot(data=df, x=exp, y=res, hue=res, palette='winter', legend=False)
    x = np.array([min(df.age.values), max(df.age.values)])
    y = predict(x)
    plt.plot(x, y)

# studying age's influence on the resting blood sugar pressure
age_train, age_test, bps_train, bps_test = train_test_split(df.age.values.reshape(-1,1), df.trtbps.values,
                                                            test_size = 0.1, random_state = 0)
gp_A_num_splitshape(df.age.values.reshape(-1,1), df.trtbps.values)
gp_A_num_regression(age_train, age_test, bps_train, bps_test)
gp_A_num_prediction(60,age_train, bps_train)
gp_A_num_scat("age","trtbps",age_train,bps_train)

# studying age's influence on the cholestoral in mg/dl
aeg_train, age_test, chol_train, chol_test = train_test_split(df.age.values.reshape(-1,1), df.chol.values,
                                                              test_size = 0.1, random_state = 0)
gp_A_num_splitshape(df.age.values.reshape(-1,1), df.chol.values)
gp_A_num_regression(age_train, age_test, chol_train, chol_test)
gp_A_num_prediction(60,age_train, chol_train)
gp_A_num_scat("age","chol",age_train,chol_train)

plt.show()

# Group A: all numerical variables influence on output

# some modifications on the dummy variables
df_mod = df.copy()
df_mod = pd.get_dummies(df_mod, columns = cat_var[:-1], drop_first = True)
print(df_mod.head())

X_num = df_mod.drop(["output"], axis=1)
y_out = df_mod[["output"]]

# scaling numeric variables for logistic regression analysis
scale = StandardScaler()
X_num[num_var[:-1]] = scale.fit_transform(X_num[num_var[:-1]])
print(X_num.head())

# splitting training and testing sets
X_num_train, X_num_test, output_train, output_test = train_test_split(X_num, y_out,
                                                                      test_size = 0.1, random_state = 2)
# logistic regression is used since the response variable output is binary
logistic = LogisticRegression()
logistic.fit(X_num_train, output_train)

out_predicted_prob = logistic.predict_proba(X_num_test)
print(out_predicted_prob)

out_predicted = np.argmax(out_predicted_prob, axis = 1)
print(out_predicted)
out_expected = output_test

print("Test accuracy: {}".format(accuracy_score(out_predicted, out_expected)))

