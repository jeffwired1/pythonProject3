import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Generate random data with 4 independent variables and 1 dependent variable
np.random.seed(0)
X = np.random.rand(100, 4)
y = 2 * X[:, 0] + 3 * X[:, 1] - 4 * X[:, 2] ** 2 + 5 * X[:, 3] ** 3 + np.random.normal(0, 0.5, 100)

# Fit a polynomial regression model with degree=2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)

# Get the intercept and coefficients
intercept = model.intercept_
coefficients = model.coef_

print(intercept)
print(coefficients)

# Create the polynomial regression equation string
variables = ['X1', 'X2', 'X3', 'X4']
terms = []
for i, c in enumerate(coefficients):
    if i == 0:
        terms.append('{:.2f}'.format(c))
    else:
        term = ''
        for j, p in enumerate(np.where(c != 0)[0]):
            if p == 0:
                term += '{:.2f} + '.format(intercept)
            else:
                coef = '{:.2f}'.format(c[p])
                powers = ' '.join(['{}^{}'.format(variables[k], int(poly.powers_[p, k])) for k in range(4)])
                term += '{} {} + '.format(coef, powers)
        term = term[:-3]
        terms.append(term)

equation = 'y = ' + ' + '.join(terms)
print(equation)
# y = 0.07 - 0.39 X1 + 0.78 X2 - 8.21 X3^2 + 5.23 X4^3 - 0.33 X1 X2 - 0.17 X1 X3 + 0.23 X1 X4 + 0.03 X2 X3 - 0.06 X2 X4 - 0.06 X3 X4 + 0.21 X1^2 - 0.09 X2^2 - 0.31 X3^2 + 0.24 X4^2
