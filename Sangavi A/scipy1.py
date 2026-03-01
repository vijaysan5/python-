import numpy as np

# 1. scipy.constants
# Used to access predefined scientific constants

from scipy import constants

print("\n--- scipy.constants ---")
print("Pi value:", constants.pi)
print("Speed of light (m/s):", constants.c)
print("Gravitational constant:", constants.G)
print("Avogadro number:", constants.Avogadro)


# 2. scipy.linalg (Linear Algebra)
# Used for advanced matrix operations

from scipy import linalg

A = np.array([[2, 1],
              [1, 3]])

print("\n--- scipy.linalg ---")
print("Matrix A:\n", A)
print("Determinant:", linalg.det(A))
print("Inverse:\n", linalg.inv(A))
print("Eigen values:", linalg.eig(A)[0])

# Solving linear equation Ax = b
b = np.array([8, 13])
x = linalg.solve(A, b)
print("Solution of Ax = b:", x)


# 3. scipy.optimize
# Used for optimization (min/max) and root finding

from scipy.optimize import root, minimize

# Root finding
def equation(x):
    return x**2 - 9

root_result = root(equation, 0)
print("\n--- scipy.optimize ---")
print("Root of equation x^2 - 9:", root_result.x)

# Minimization
def func(x):
    return x**2 + 4*x + 5

min_result = minimize(func, 0)
print("Minimum value occurs at:", min_result.x)


# 4. scipy.stats
# Used for statistics and probability distributions

from scipy import stats

data = [10, 20, 20, 30, 40]

print("\n--- scipy.stats ---")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)
print("Standard Deviation:", np.std(data))

# Normal distribution
print("Normal PDF at x=0:", stats.norm.pdf(0))
print("Normal CDF at x=1:", stats.norm.cdf(1))


# 5. scipy.integrate
# Used for mathematical integration

from scipy.integrate import quad

def square(x):
    return x**2

result, error = quad(square, 0, 3)

print("\n--- scipy.integrate ---")
print("Integration of x^2 from 0 to 3:", result)


# 6. scipy.interpolate
# Used to estimate unknown values between known data points

from scipy.interpolate import interp1d

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

interp_func = interp1d(x, y)

print("\n--- scipy.interpolate ---")
print("Interpolated value at x=2.5:", interp_func(2.5))


# 7. scipy.cluster (CLUSTERING CONCEPTS)
# SciPy provides hierarchical clustering

from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist

# Sample data points
points = np.array([
    [1, 2],
    [2, 3],
    [5, 8],
    [6, 9]
])

print("\n--- scipy.cluster (Hierarchical Clustering) ---")

# Distance calculation
distance_matrix = pdist(points)
print("Pairwise distances:", distance_matrix)

# Linkage (hierarchical clustering)
linked = linkage(points, method="ward")

# Form clusters
clusters = fcluster(linked, t=2, criterion="maxclust")
print("Cluster labels:", clusters)