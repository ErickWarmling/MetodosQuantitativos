from pyomo.environ import *

# Volume do pedido
V = 100
# Teor alcoólico desejado
A = 0.06

componentes = {
    'Cerveja A': {'A': 0.058,'P': 0.28},
    'Cerveja B': {'A': 0.037, 'P': 0.25},
    'Água': {'A': 0.000, 'P': 0.25},
    'Vinho': {'A': 0.083, 'P': 0.40}
}

C = componentes.keys()

# Modelo
model = ConcreteModel()

#Variáveis de decisão
model.x = Var(C, domain=NonNegativeReals)

# Função objetivo
model.obj = Objective(expr= sum(model.x[c] * componentes[c]['P'] for c in C))

# Restrições
model.const1 = Constraint(expr= sum(model.x[c] for c in C) == V)
model.const2 = Constraint(expr= sum(model.x[c] * componentes[c]['A'] for c in C) == A * V)

solver = SolverFactory('glpk', executable="C:/glpk/glpk-4.65/w64/glpsol.exe")
solver.solve(model)

print('Mistura ótima')
for c in C:
    print('>', c, ':', model.x[c](), 'litros')
print()
print('Volume =', model.const1(), 'litros')
print('Custo = $', model.obj())