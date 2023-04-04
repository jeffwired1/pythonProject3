from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# create some sample data
X = [[1, 2, 3, 4],
     [2, 3, 4, 5],
     [3, 4, 5, 6],
     [4, 5, 6, 7],
     [5, 6, 7, 8]]
y = [2, 3, 4, 5, 6]

# create polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# fit linear regression model
model = LinearRegression()
model.fit(X_poly, y)

# get coefficients and intercept
coef = model.coef_
intercept = model.intercept_

print(intercept)
print(coef)



y = b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b12*x1*x2 + b13*x1*x3 + b14*x1*x4 + b23*x2*x3 + b24*x2*x4 + b34*x3*x4 + b11*x1^2 + b22*x2^2 + b33*x3^2 + b44*x4^2


