import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Define the data
from sklearn.utils.extmath import safe_sparse_dot

x1 = np.array([1, 1.1, 1.1, 1.2, 1.2])
x2 = np.array([2,2,2,2,2])
x3 = np.array([3, 3, 3, 3, 3])
x4 = np.array([4, 4, 4, 4, 4])
y = np.array([2,2.1,2.1,2.2,2.6])

# Create the design matrix
X = np.column_stack((x1, x2, x3, x4))
poly = PolynomialFeatures(degree=2)
X_design = poly.fit_transform(X)

# Fit the linear regression model
model = LinearRegression()
model.fit(X_design, y)

# Print the model coefficients
intercept = model.intercept_
coeff = model.coef_
print(model.intercept_)
print(model.coef_)

n = 0

x1 = x1[n]
x2 = x2[n]
x3 = x3[n]
x4 = x4[n]
y = y[n]

-0.33 + 0.17x1 + 0.25x2 + 0.08x3 + 0.01x1^2 + 0.05x1x2 -0.01x1x3 + 0.03x2^2 + 0.01x2x3 + 0.00x3^2 -0.03x1x4 + 0.02x2x4 + 0.00x3x4 + 0.02x4^2


row = intercept \
    + coeff[1]*x1 + coeff[2]*x2  + coeff[3]*x3 + coeff[4]*x4 \
    + coeff[5]*x1*x1 + coeff[6]*x2*x2 + coeff[7]*x3*x3 + coeff[8]*x4*x4 \
    + coeff[9]*x1*x2 + coeff[10]*x1*x3 + coeff[11]*x1*x4 \
    + coeff[12]*x2*x3 + coeff[13]*x2*x4 + coeff[14]*x3*x4

print(row, x1,x2,x3,x4,y)


# print(f'Response surface equation: {intercept:.2f} + {coeff[0]:.2f}x1 + {coeff[1]:.2f}x2 + {coeff[2]:.2f}x3\
# + {coeff[3]:.2f}x4 + {coeff[4]:.2f}x1^2 + {coeff[5]:.2f}x2^2 + {coeff[6]:.2f}x3^2 + {coeff[7]:.2f}x4^2\
 #   + {coeff[8]:.2f}x1*X2 + {coeff[9]:.2f}x1*x3 + {coeff[10]:.2f}x1*x3 + {coeff[11]:.2f}x1*x4\
#    + {coeff[12]:.2f}x2*x3 + {coeff[13]:.2f}x2*x4 + {coeff[14]:.2f}x3*x4')





l = model.predict(X_design)
print(l)



