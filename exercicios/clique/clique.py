from pyomo.environ import *

# Vértices
V = {1, 2, 3, 4, 5, 6}
# Arestas
E = {(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6)}
# Peso dos vértices
C = {1: 4, 2: 5, 3: 6, 4: 3, 5: 2, 6: 7}

model = ConcreteModel()

# Variáveis de decisão
model.x = Var(V, domain=Binary)

# Função objetivo
model.obj = Objective(expr=sum(C[v] * model.x[v] for v in V), sense=minimize)

# Restrições
model.const = ConstraintList()

for u in V:
    for v in V:
        if (u, v) not in E:
            model.const.add(expr=model.x[u] + model.x[v] <= 1)

solver = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
solver.solve(model)

print('Função objetivo: ', model.obj())
for v in V:
    if model.x[v].value == 1:
        print(f'Vértice {v} está incluído no clique')
    else:
        print(f'Vértice {v} não está incluído no clique')