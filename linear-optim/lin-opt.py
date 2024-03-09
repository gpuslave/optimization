import numpy as np
from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# # Coefficients of the objective function
# c = [-1, -3]  # Note the negative signs for maximization

# # Inequality constraints matrix
# A = [[3, 7], [2, 8]]

# # Inequality constraints vector
# b = [200, 400]

# # Bounds for variables
# x0_bounds = (0, None)
# x1_bounds = (0, None)

# res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# print('Optimal value:', -res.fun, '\nX:', res.x[0], res.x[1])


# model definition
model1 = LpProblem(name="small-problem", sense=LpMinimize)

# decision variables: x1 and x2 in range [0, inf)
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)

# constraints
model1 += (3*x1 + 2*x2 >= 10, "constraint1")
model1 += (4*x1 + 6*x2 >= 10, "constraint2")
model1 += (x1 + 3*x2 >= 7, "constraint3")

# objective func
model1 += lpSum([3*x1, 4*x2])

status = model1.solve()

print(f"status: {model1.status}, {LpStatus[model1.status]}")
print(f"objective: {model1.objective.value()}")

for var in model1.variables():
    print(f"{var.name}: {var.value()}")

# # model definition
# model = LpProblem(name="small-problem", sense=LpMaximize)

# # decision variables: x1 and x2 in range [0, inf)
# y1 = LpVariable(name="y1", lowBound=0)
# y2 = LpVariable(name="y2", lowBound=0)
# y3 = LpVariable(name="y3", lowBound=0)

# # constraints
# model += (3*y1 + 4*y2 + y3 <= 3, "constraint1")
# model += (2*y1 + 6*y2 + 3*y3 <= 4, "constraint2")

# # objective func
# model += lpSum([10*y1, 10*y2, 7*y3])

# status = model.solve()

# print(f"status: {model.status}, {LpStatus[model.status]}")
# print(f"objective: {model.objective.value()}")

# for var in model.variables():
#     print(f"{var.name}: {var.value()}")
