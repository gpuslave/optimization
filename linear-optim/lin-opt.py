import numpy as np
from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Coefficients of the objective function
c = [-1, -3]  # Note the negative signs for maximization

# Inequality constraints matrix
A = [[3, 7], [2, 8]]

# Inequality constraints vector
b = [200, 400]

# Bounds for variables
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print('Optimal value:', -res.fun, '\nX:', res.x[0], res.x[1])


# model definition
model = LpProblem(name="small-problem", sense=LpMaximize)

# decision variables: x1 and x2 in range [0, inf)
x1 = LpVariable(name="x1", lowBound=0, cat='Integer')
x2 = LpVariable(name="x2", lowBound=0, cat='Integer')

# constraints
model += (3 * x1 + 7 * x2 <= 200, "constraint1")
model += (2 * x1 + 8 * x2 <= 400, "constraint2")

# objective func
model += lpSum([x1, 3 * x2])

status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")
