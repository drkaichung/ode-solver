import math

from sympy import symbols, Function, plot, Derivative, Eq, dsolve, sympify, sin, cos, solve, pi, I, E, exp


x= symbols('x')
t = symbols('t')
y= Function('y', real = True)
c1,c2= symbols('C1'), symbols('C2')


while True:
    expression =(input("What is your function?: "))
    try:
        if "=" in expression:
            lhs, rhs = expression.split("=")
            expression = Eq(sympify(lhs, locals={'x':x,'t':t,'y':y(x), 'exp': exp}), sympify(rhs, locals={'x':x,'t':t, 'y':y(x), 'exp': exp}))
        else:
            expresion = sympify(expression, locals={'x':x,'t':t,'y':y(x),'exp': exp})
        break

    except Exception as e:
        print("Error! Put in a valid ODE: ",e)
        continue

try:
    ode_solution= dsolve(expression,y(x))
    if isinstance(ode_solution,list):

        real_solution = []
        for sol in ode_solution:
            if not sol.rhs.has(I):
                real_solution.append(sol)
        if not real_solution:
            real_solution = ode_solution
        ode_solution = real_solution[0]

    print("This is the general solution:", ode_solution)
except Exception as e:
    print("ODE only please!",e)
    exit()

solution = ode_solution.rhs


derivative_order =  max((d.derivative_count for d in expression.atoms(Derivative)), default = 0)


particular_soln = None
if derivative_order == 0:
     print ("This is not not a valid ODE. There are no derivatives")
elif derivative_order == 1:
    y_0 = (input("Enter the first initial condition: "))
    if y_0 != "":
        y0 = sympify(y_0)
        c1_value = solve(solution.subs(x,0) -  y0,c1)[0]
        particular_soln = solution.subs(c1, c1_value)
        print("particular solution:", particular_soln)

elif derivative_order == 2:
    y_0 = (input("Enter the first initial condition: "))
    y_1 =(input("Enter the second initial condition: "))
    if y_0 != "" and y_1 !="":
        y0 = sympify(y_0)
        dy0 = sympify(y_1)
        equations = [solution.subs(x,0)-y0,
                     solution.diff(x).subs(x,0)-dy0]
        c_values= solve(equations, [c1,c2])
        particular_soln = solution.subs(c_values)
        print("particular solution: ", particular_soln)

else:
    print("General solution with no initial conditions", ode_solution)

if particular_soln is None:
    print("No plot: No particular solution")
else:
    plotable_equation = plot(particular_soln, (x,0,5), title = "y(x)=" + str(particular_soln),xlabel = 'x', ylabel = 'y(x)') #this starts at 0 and ends at 10
    plotable_equation.show()







