from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1, 2], domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = model.x[1] + 25 * model.x[2], sense = maximize)

# Restrições
model.const1 = Constraint(expr = 15 * model.x[1] + 300 * model.x[2] <= 10000)
model.const2 = Constraint(expr = model.x[1] - 2 * model.x[2] >= 0)
model.const3 = Constraint(expr = model.x[1] <= 400)

# Solução
opt = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
results = opt.solve(model)

print('\nSolução Ótima')
print('Anúncio Rádio: ', model.x[1].value)
print('Anúncio TV: ', model.x[2].value)
print('Alocação ótima da verba: ', model.obj.expr())