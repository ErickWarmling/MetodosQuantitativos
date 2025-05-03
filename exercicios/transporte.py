from pyomo.environ import *

# Fornecedores
m = 3
# Clientes
n = 3
# Estoques
a = [5, 7, 3]
# Demandas
b = [7, 3, 5]
# Custos
c = [[3, 1, 100],
     [4, 2, 4],
     [100, 3, 3]]

model = ConcreteModel()

# Variáveis de decisão
model.x = Var([i for i in range(m)], [j for j in range(n)], domain=NonNegativeReals)

def funcaoObjetivo(model):
    resultado = 0
    for i in range(m):
        for j in range(n):
            resultado += c[i][j] * model.x[i,j]
    return resultado

# Função objetivo
model.obj = Objective(rule = funcaoObjetivo, sense=minimize)

# Restrições
model.const = ConstraintList()

for i in range(m):
    model.const.add(sum(model.x[i,j] for j in range(n)) <= a[i])

for j in range(n):
    model.const.add(sum(model.x[i,j] for i in range(m)) == b[j])

solver = SolverFactory('glpk', executable="C:/glpk/glpk-4.65/w64/glpsol.exe")
solver.solve(model)

print('Custo: ', model.obj())
for i in range(m):
    for j in range(n):
        print(i + 1, '-->', j + 1, ':', model.x[i,j]())