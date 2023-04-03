import numpy as np
import matplotlib.pyplot as plt

# Define the four-variable function to generate data from
def func(x1, x2, x3, x4):
    return 2 + 3*x1 + 4*x2 + 5*x3 + 6*x4 + 7*x1**2 + 8*x2**2 + 9*x3**2 + 10*x4**2 + 11*x1*x2 + 12*x1*x3 + 13*x1*x4 + 14*x2*x3 + 15*x2*x4 + 16*x3*x4

# Generate data for x1, x2, x3, and x4
x1 = 1,1,1,1,1
x2 = 2,2,2,2,2
x3 = 3,3,3,3,3
x4 = 4,4,4,4,4
x1, x2, x3, x4 = np.meshgrid(x1, x2, x3, x4)

# Generate corresponding y values using the function
y = func(x1, x2, x3, x4)

# Fit a quadratic response surface equation to the data
X = np.column_stack((np.ones_like(x1.ravel()), x1.ravel(), x2.ravel(), x3.ravel(), x4.ravel(),
                     x1.ravel()**2, x2.ravel()**2, x3.ravel()**2, x4.ravel()**2,
                     x1.ravel()*x2.ravel(), x1.ravel()*x3.ravel(), x1.ravel()*x4.ravel(),
                     x2.ravel()*x3.ravel(), x2.ravel()*x4.ravel(), x3.ravel()*x4.ravel()))
p, _, _, _ = np.linalg.lstsq(X, y.ravel(), rcond=None)

# Print the response surface equation
print('y = %.3f + %.3f*x1 + %.3f*x2 + %.3f*x3 + %.3f*x4 + %.3f*x1^2 + %.3f*x2^2 + %.3f*x3^2 + %.3f*x4^2 + %.3f*x1*x2 + %.3f*x1*x3 + %.3f*x1*x4 + %.3f*x2*x3 + %.3f*x2*x4 + %.3f*x3*x4' % tuple(p))
print(x2)

