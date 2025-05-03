from pyomo.environ import *

# Criação do Modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1, 2], domain = NonNegativeReals)

# Função objeitvo
model.obj = Objective(expr = model.x[1] + 2 * model.x[2], sense = maximize)

# Restrições
model.const1 = Constraint(expr = model.x[1] + model.x[2] <= 10)
model.const2 = Constraint(expr = model.x[1] - model.x[2] >= 0)
model.const3 = Constraint(expr = model.x[2] <= 4)

# Solução

opt = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
results = opt.solve(model)

print('\nSolução Ótima')
print('Estudo: ', model.x[1].value)
print('Diversão: ', model.x[2].value)
print('Tempo dispónivel alocado: ', model.obj.expr())