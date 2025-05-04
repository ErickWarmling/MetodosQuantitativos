from pyomo.environ import *

# Vértices
V = ['A', 'B', 'C', 'D', 'E']
# Arestas
E = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('C', 'D'), ('D', 'E')}
# Custo das arestas
C = {('A', 'B'): 3, ('A', 'C'): 2, ('A', 'D'): 1, ('C', 'D'): 6, ('D', 'E'): 5}

model = ConcreteModel()

# Variáveis de decisão
model.x = Var(E, domain=Binary)

# Função objetivo
model.obj = Objective(expr=sum(C[u, v] * model.x[u, v] for (u, v) in E), sense=minimize)

# Restrições
model.const = ConstraintList()

for vertice in V:
    model.const.add(expr=sum(model.x[u, v] for (u,v) in E if u == vertice or v == vertice) >= 1)

solver = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
solver.solve(model)

print('Função objetivo: ', model.obj())
print('Cobertura por arestas:')
for (u, v) in E:
    if model.x[u, v].value == 1:
        print(f'({u}, {v}) com custo {C[(u, v)]}')