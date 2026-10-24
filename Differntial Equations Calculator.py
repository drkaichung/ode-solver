import math

from sympy import symbols, Function, Eq, dsolve, sympify, sin, cos, solve, pi




x= symbols('x')
t = symbols('t')
y= Function('y')
c1 = symbols('C1')


while True:
    text =(input("What is your function?: "))
    try:
        expression =sympify(text, locals={'x':x,'t':t,'y':y(x),
                            'sin': sin, 'cos': cos})
        break
    except Exception as e:
        print("Error! Put in a valid ODE: ",e)
        continue
try:
    ode_solution= dsolve(expression,y(x))
    print("This is the general solution:", ode_solution)

except Exception as e:
    print("ODE only please!",e)

y0 = sympify(input("Enter the initial condition:"))

if y0 != "":
    eq = ode_solution.subs(x,0)
    eq2 = eq.subs(y(0),y0)
    c1_value = solve(eq2, c1)[0]
    particular_soln = ode_solution.subs(c1, c1_value)
    print("particular solution", particular_soln)
else:
    print("General solution with no initial conditions", ode_solution)








