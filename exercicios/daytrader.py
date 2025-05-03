from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1, 2], domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = model.x[1] + model.x[2], sense = minimize)

# Restrições
model.const1 = Constraint(expr = 0.1 * model.x[1] + 0.25 * model.x[2] >= 10000)
model.const2 = Constraint(expr = -0.6 * model.x[1] + 0.4 * model.x[2] <= 0)

# Solução
opt = SolverFactory('glpk', executable='C:/glpk/glpk-4.65/w64/glpsol.exe')
results = opt.solve(model)

print('\nSolução Ótima')
print('Grupo Primeira Linha: ', model.x[1].value)
print('Grupo Alta Tecnologia: ', model.x[2].value)
print('Quantidade mínima de investimento em cada grupo: ', model.obj.expr())