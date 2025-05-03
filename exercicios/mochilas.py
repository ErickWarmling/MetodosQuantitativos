from pyomo.environ import *

# Número de mochilas
m = 10
# Número de itens
n = 10
# Capacidade da mochila j
c = [5, 7, 6, 8, 10, 9, 5, 6, 7, 8]
# Valor do item i
v = [10, 15, 20, 25, 18, 12, 30, 22, 16, 14]
# Peso do item i
p = [2, 3, 4, 5, 3, 2, 6, 4, 3, 2]

model = ConcreteModel()

# Variáveis de decisão
model.x = Var([i for i in range(n)], [j for j in range(m)], domain=Binary)

# Função objetivo
def funcaoObjetivo(model):
    resultado = 0
    for j in range(m):
        for i in range(n):
            resultado += v[i] * model.x[i, j]
    return resultado

model.obj = Objective(rule = funcaoObjetivo, sense=maximize)

# Restrições
model.const = ConstraintList()

for j in range(m):
    model.const.add(sum(p[i] * model.x[i, j] for i in range(n)) <= c[j])

for j in range(m):
    model.const.add(sum(model.x[i, j] for i in range(n)) <= 1)

solver = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
solver.solve(model)

print('Função Objetivo: ', model.obj.expr())
for j in range(m):
    print(f'Mochila {j + 1} (Capacidade: {c[j]})')
    for i in range(n):
        if model.x[i, j].value == 1:
            print(f'Item {i + 1} alocado')
        else:
            print(f'Item {i + 1} não alocado')
    print()