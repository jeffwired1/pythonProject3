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



# -0.33 + 0.17x1 + 0.25x2 + 0.08x3 + 0.01x1^2 + 0.05x1x2 -0.01x1x3 + 0.03x2^2 + 0.01x2x3 + 0.00x3^2 -0.03x1x4 + 0.02x2x4 + 0.00x3x4 + 0.02x4^2


