from pyomo.environ import *

# Tipos de grão
m = 10
# Capacidade (massa) do caminhão
T = 28
# Capacidade (volume) do caminhão
V = 83
# Densidade do grão i
D = [1.3, 0.7, 1.8, 1.1, 1.0, 1.5, 0.9, 0.8, 1.0, 1.2]
# Volume máximo do grão i
Q = [10, 12, 40, 21, 5, 5, 8, 17, 6, 9]
# Receita esperada do grão i
R = [5, 3, 2.2, 4, 1.8, 4.1, 3.7, 1.9, 6, 2]

model = ConcreteModel()

# Variáveis de decisão
model.x = Var(range(m), domain=NonNegativeReals)

# Função objetivo
model.obj = Objective(expr= sum(model.x[i] * R[i] for i in range(m)), sense=maximize)

# Restrições
model.const = ConstraintList()

model.const.add(expr= sum(model.x[i] for i in range(m)) <= V)
model.const.add(expr= sum(model.x[i] * D[i] for i in range(m)) <= T)
for i in range(m):
    model.const.add(model.x[i] <= Q[i])

solver = SolverFactory('glpk', executable="C:/glpk/glpk-4.65/w64/glpsol.exe")
solver.solve(model)

print('Função objetivo: ', model.obj())
for i in range(m):
    print(f'Grão {i + 1}: {model.x[i]()} m3')