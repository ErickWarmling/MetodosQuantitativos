from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1, 2], domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = 1500 * model.x[1] + 1000 * model.x[2], sense = maximize)

# Restrições
model.const1 = Constraint(expr = model.x[1] + model.x[2] <= 30)
model.const2 = Constraint(expr = model.x[1] >= 10)
model.const3 = Constraint(expr = model.x[2] >= 10)

# Solução
opt = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
results = opt.solve(model)

print('\nSolução Ótima')
print('Cursos Práticos: ', model.x[1].value)
print('Cursos Humanas: ', model.x[2].value)
print('Lucro: ', model.obj.expr())