import gekko
import numpy as np

# m = gekko.GEKKO(remote=False)

# y1 = 10
# y2 = 12
# y3 = 14

# #initialize variables
# b1,b2,b3 = [m.Var(value=0.5, lb=0.1, ub=0.4) for i in range(3)]


# m.Equation(b1 + b2 + b3 == 1)

# obj = b1*y1 + b2*y2 + b3*y3
# m.Minimize(-obj)

# m.solve()

# obj_value = b1.value[0]*y1 + b2.value[0]*y2 + b3.value[0]*y3

# print(b1.value)
# print(b2.value)
# print(b3.value)
# print(obj_value)


'''------------Matrix form------------'''

m = gekko.GEKKO(remote=False)

y = np.array([10, 12, 14])

# Variables (in matrix form)
b = m.Array(m.Var, 3, lb=0.1, ub=0.4)
# b = np.array(b) # not neccessary

# Constraint in matrix form
m.Equation(np.sum(b) == 1)

# Objective function in matrix form
obj = np.dot(b, y)
m.Minimize(-obj)


# Solve the optimization problem
m.solve(disp=False)

# Extracting Results
b_optimized = np.array([bi.value[0] for bi in b])
obj_value = np.dot(b_optimized, y)

# Print Results
print("Optimized b:", b_optimized)
print("Optimized Objective Value:", obj_value)


