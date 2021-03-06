# Exercise #01
In this exercise, you will train a supervised regression machine learning to predict the price of houses in Portland/USA. The file "prices.txt" contains the dataset you will use to create a regression model.

1) Use Numpy to read the dataset as a matrix. See numpy.loadtxt() function. The first column contains the house size in square meters (X) and the second column contains the price of houses in dollars (Y).

2) Plot your data set as red crosses. See matplotlib.pyplot.plot() function.

3) Use linear regression to fit your dataset. You can develop your own code using Ordinary Least Square (OLS) or scikit-learn (http://scikit-learn.org/stable/modules/linear_model.html).

4) Use a second order polynomial to fit your dataset. See sklearn.preprocessing.PolynomialFeatures() function (http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

5) Predict the price of a house with 1.250 m2 and 100.000 m2 (Neverland Ranch) using linear and second order regression. Compare the values returned by each model.

# Exercise #02
In this exercise, you will develop an unsupervised clustering machine learning to classify the urban and rural drivers. The file "drivers.txt" contains the dataset you will use to create a clustering model.

1) Use Numpy to read the dataset as an array. See numpy.loadtxt() function. The first column contains the average distance in kilometers (X) and the second column contains the average speed in kilometers (Y).

2) Use K-Means to classify your dataset into two groups (i.e. rural and urban). You can develop your own code based on the pseudocode available in the slides or using scikit-learn (http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html).

3) Test your dataset with a different number of clusters (N > 2).
