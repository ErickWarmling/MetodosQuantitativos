from pyomo.environ import *
import sys

graph = []
n = None
v = None

instance = open(sys.argv[1], 'r')
for line in instance.readlines():
    if line.startswith('c'): continue
    if line.startswith('p'):
        line = line.strip().split(' ')
        n = int(line[2])
        v = list(range(n))
        for _ in range(n):
            graph.append([0] * n)
        continue
    line = line.strip().split(' ')
    if len(line) == 2:
        u, w = int(line[0]) - 1, int(line[1]) - 1
        graph[u][w] = 1
        graph[w][u] = 1

model = ConcreteModel()

# Variáveis de decisão
model.x = Var(v, domain=Binary)

# Função objetivo
model.obj = Objective(expr=sum(model.x[i] for i in v), sense=minimize)

# Restrições
model.const = ConstraintList()

for i in v:
    model.const.add(expr=model.x[i] + sum(model.x[j] for j in v if graph[i][j] == 1) >= 1)

solver = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
solver.solve(model)

print('Função objetivo: ', model.obj())
conjuntoDominante = []
for i in v:
    if model.x[i].value == 1:
        conjuntoDominante.append(i + 1)
print("Conjunto dominante: ", conjuntoDominante)
