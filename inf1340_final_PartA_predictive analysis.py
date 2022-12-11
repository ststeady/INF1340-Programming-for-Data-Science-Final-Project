import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, \
    confusion_matrix, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Part A studying variables: age,cp,trtbps,chol,output
# Part B studying variables: sex,exang,thalach,oldpeak,output
# Sub-groups study may not be limited to the above variables...

df = pd.read_csv("heart.csv")
print(df.head())

# print out the correlation matrix and deciding which variables to study
corr_matrix = df.corr()
print(corr_matrix)

# visualizing the correlation matrix
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, cmap="BuPu", annot=True, mask=mask)

# visualizing the variables distribution
color = '#9A32CD'
df.hist(bins=15, figsize=(25, 15), color=color)
plt.rcParams['font.size'] = 20

# Group A: numerical variables and categorical variables
num_var = ["age", "trtbps", "chol"]
cat_var = ["cp", "slp", "output"]


# Group A: splitting shape printing function
def gp_A_num_splitshape(X, y):
    '''This function takes the parameters of two numpy arrays, where X is explanatory variable, and
    Y is response variable. The function then split X and y into training and testing datasets and
    print out the shape of the split.
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    print("The training set X has shape" + str(X_train.shape) + "\n" +
          "The testing set X has shape" + str(X_test.shape) + "\n" +
          "The training set y has shape" + str(y_train.shape) + "\n" +
          "The testing set y has shape" + str(y_test.shape) + "\n")


# Group A: predicted value and expected value function
def gp_A_num_regression(X_train, X_test, y_train, y_test):
    '''This function takes the parameters of four numpy arrays, which are the splited X training sets,
    x testing sets, y training sets and y testing sets, respectively. The function then fit the training sets
    into a linear regression model, and compare and print the predicted results with the testing sets.
    '''
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    predicted = linear_regression.predict(X_test)
    expected = y_test
    for i, j in zip(predicted[::5], expected[::5]):
        print(f'predicted:{i:2f}, expected:{j:.2f}')
    print("\n")


def gp_A_num_prediction(age, X_train, y_train):
    '''This function takes the parameters of a numeric variable, and two numpy arrays. The
    numeric variable is an age from users' input, and the two arrays are the splited training
    data sets for X and y. With the fitted linear regression model, the function returns the
    predicted value of the response variable given the age entered.
    '''
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    predict = (lambda i: linear_regression.coef_ * i + linear_regression.intercept_)
    print("The predicted value at age " + str(age) + " is " + str(predict(age)))


# Group A: scatterplot of final prediction accuracy function
def gp_A_num_scat(exp, res, X_train, y_train):
    '''This function takes the parameters of two strings, and two numpy arrays. The strings are
    variable names of the explantory variable and response variable as in the dataframe, and the
    two arrays are splited training datasets for X and y. With the fitted linear regression model,
    the function plots a scatterplot of the entered variables, with a line representing the fitted
    linear regression model.
    '''
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    predict = (lambda i: linear_regression.coef_ * i + linear_regression.intercept_)
    plt.figure(figsize=(8, 4.5))
    sns.scatterplot(data=df, x=exp, y=res, hue=res, palette='winter', legend=False)
    x = np.array([min(df.age.values), max(df.age.values)])
    y = predict(x)
    plt.plot(x, y)


# studying age's influence on the resting blood sugar pressure
# split the training and testing data sets for age and blood sugar pressure
age_train, age_test, bps_train, bps_test = train_test_split(df.age.values.reshape(-1, 1), df.trtbps.values,
                                                            test_size=0.1, random_state=0)
gp_A_num_splitshape(df.age.values.reshape(-1, 1), df.trtbps.values)
gp_A_num_regression(age_train, age_test, bps_train, bps_test)
gp_A_num_prediction(60, age_train, bps_train)
gp_A_num_scat("age", "trtbps", age_train, bps_train)

# studying age's influence on the cholestoral in mg/dl
# split the training and testing data sets for age and cholestoral
aeg_train, age_test, chol_train, chol_test = train_test_split(df.age.values.reshape(-1, 1), df.chol.values,
                                                              test_size=0.1, random_state=0)
gp_A_num_splitshape(df.age.values.reshape(-1, 1), df.chol.values)
gp_A_num_regression(age_train, age_test, chol_train, chol_test)
gp_A_num_prediction(60, age_train, chol_train)
gp_A_num_scat("age", "chol", age_train, chol_train)

# Group A: all selected variables' impact on output

# modified dataframe for dummy variables
df_mod = df[["age", "trtbps", "chol", "cp", "slp", "output"]]
df_mod = pd.get_dummies(df_mod, columns=cat_var[:-1], drop_first=True)

# get an array for explanatory variables and response variable
X_exp = df_mod.drop(["output"], axis=1)
y_out = df_mod[["output"]]

# scaling numeric variables for logistic regression analysis
scale = StandardScaler()
X_exp[num_var[:-1]] = scale.fit_transform(X_exp[num_var[:-1]])
print(X_exp)

# splitting training and testing sets
X_exp_train, X_exp_test, output_train, output_test = train_test_split(X_exp, y_out,
                                                                      test_size=0.1, random_state=2)
# logistic regression is used since the response variable output is binary
logistic = LogisticRegression(max_iter=200)
logistic.fit(X_exp_train, output_train.values.ravel())

# print the prediction interval
out_predicted_prob = logistic.predict_proba(X_exp_test)
print(out_predicted_prob)
# expected and prediction comparison
out_predicted = np.argmax(out_predicted_prob, axis=1)
print(out_predicted)
out_expected = output_test

# Test the accuracy of the suggested model
print("Test accuracy: {}".format(accuracy_score(out_predicted, out_expected)))

# Plotting the confusion matrix
confusion = confusion_matrix(output_test, out_predicted, labels=logistic.classes_)
display = ConfusionMatrixDisplay(confusion_matrix=confusion, display_labels=logistic.classes_)
display.plot()

# Plotting the ROC curve
# calculating false positive, true positive, and classification thresholds
fpr, tpr, thresholds = roc_curve(output_test, out_predicted_prob[:, 1])
plt.figure(figsize=(8, 4.5))
plt.plot([0, 1], [0, 1], "k--")
plt.plot(fpr, tpr, label="Logistic Regression")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Fitted Logistic Regression Model")
plt.show()

# The ROC curve tells us that most of our predictions are accurate compared to the testing response value
# since the curve shows a logarithmic growth, meaning that we have more accurate predictions rather than
# type I error.

# Conclusion: If we define age as an explanatory variable, the resting blood pressure (in mm Hg) and cholestoral (in
# mg/dl) is expected to have a positive relationship with age, meaning that as age increases, resting blood pressure
# and cholestoral level will also increase, and the scatterplots also consist with the increasing trend. Furthermore,
# when we fit the selected variables to build a logistic model for the output variable (that is, fitting "age",
# "trtbps", "chol", "cp", "slp" to the response "output"), the model could reach an accuracy score of 0.903. The
# prediction interval of the fitted model does not include 0, meaning that the variables are significant. Confusion
# matrix and ROC curve further proves the accuracy of the model, that the number of type I and II errors are minimized.