from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1, 2], domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = 8 * model.x[1] + 6 * model.x[2], sense = minimize)

# Restrições
model.const1 = Constraint(expr = model.x[1] >= 5)
model.const2 = Constraint(expr = model.x[1] <= 12)
model.const3 = Constraint(expr = model.x[2] >= 6)
model.const4 = Constraint(expr = model.x[2] <= 10)
model.const5 = Constraint(expr = model.x[1] + model.x[2] >= 20)

# Solução
opt = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
results = opt.solve(model)

print('\nSolução ótima')
print('Loja 1: ', model.x[1].value)
print('Loja 2: ', model.x[2].value)
print('Horas trabalhadas em cada loja: ', model.obj.expr())