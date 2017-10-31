# Import libraries.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Read the input data.
data = np.loadtxt("prices.txt", delimiter=",")
data = np.asmatrix(data)

# Minimum and maximum values
x_min  = data[:, 0].min()
x_max  = data[:, 0].max()
x_plot = np.linspace(x_min, x_max, 100)
x_plot = np.asmatrix(x_plot).T

# Plot the input data.
plt.plot(data[:, 0], data[:, 1], "rx")
plt.xlabel("Size (square meters)")
plt.ylabel("Price USD (in 1000s)")

# Linear regression.
linear = linear_model.LinearRegression()
linear.fit(data[:, 0], data[:, 1])

# Prediction.
y_plot = linear.predict(x_plot)

# Plot the linear regression line.
plt.plot(x_plot, y_plot, color="green", linewidth=3)

# Linear results.
predict1 = linear.predict(1250)
predict2 = linear.predict(100000)
print "For 1.250 square meters, we predict a price of: %.2f." % (predict1)
print "For 100.000 square meters, we predict a price of: %.2f." % (predict2)

# Second order regression.
model = make_pipeline(PolynomialFeatures(2), Ridge())
model.fit(data[:, 0], data[:, 1])

# Prediction.
y_plot = model.predict(x_plot)

# Plot the second order regression curve.
plt.plot(x_plot, y_plot, color="blue", linewidth=3)

# Linear results.
predict1 = model.predict(1250)
predict2 = model.predict(100000)
print "For 1.250 square meters, we predict a price of: %.2f." % (predict1)
print "For 100.000 square meters, we predict a price of: %.2f." % (predict2)

plt.legend(["Training Data", "Linear", "Second Order"])
plt.show()
