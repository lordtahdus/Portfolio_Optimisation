import gekko

m = gekko.GEKKO(remote=False)

y1 = 10
y2 = 12
y3 = 14

#initialize variables
b1,b2,b3 = [m.Var(value=0.5, lb=0.1, ub=0.4) for i in range(3)]


m.Equation(b1 + b2 + b3 == 1)

obj = b1*y1 + b2*y2 + b3*y3
m.Minimize(-obj)

m.solve()

obj_value = b1.value[0]*y1 + b2.value[0]*y2 + b3.value[0]*y3

print(b1.value)
print(b2.value)
print(b3.value)
print(obj_value)
