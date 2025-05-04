from pyomo.environ import *
import sys

graph = []
T = None
C = list(range(10))
v = len(C)

# Leitura da instância
instance = open(sys.argv[1], 'r')
for line in instance.readlines():
    if line.startswith('c'): continue
    if line.startswith('p'):
        line = line.strip().split(' ')
        T = int(line[2])
        for _ in range(T):
            graph.append([0] * T)
        continue
    if line.startswith('e'):
        line = line.strip().split(' ')
        graph[int(line[1])][int(line[2])] = int(line[3])
        graph[int(line[2])][int(line[1])] = int(line[3])

model = ConcreteModel()

# Variáveis de decisão
model.x = Var([i for i in range(T)], [j for j in range(v)], domain=Binary)
model.y = Var([i for i in range(v)], domain=Binary)

# Função objetivo
model.obj = Objective(expr=sum(model.y[i] for i in range(v)), sense=minimize)

# Restrições
model.const = ConstraintList()

for i in range(T):
    model.const.add(expr=sum(model.x[i, j] for j in range(v)) == 1)

for i in range(T):
    for j in range(i + 1, T):
        if graph[i][j] != 0:
            for u in range(v):
                model.const.add(expr=model.x[i, u] + model.x[j, u] <= model.y[u])

solver = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
solver.solve(model)

print("Função objetivo: ", model.obj())
for i in range(T):
    for j in range(v):
        if model.x[i, j].value == 1:
            print(f'Vértice {i} foi colorido com a cor {j}')