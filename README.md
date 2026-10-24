#ODE Solver
A python tool that solves first and second order differntial equations

# Example
Equations: y.diff(x,2) + sin(x) * y
y(0) = 1
y'(0) = pi

Solution:
  y(x) =  pi * x * (x**2 * sin(x)/6 + 1 )

# Note
Input: Put your preferred differential equations with respect to either t or x
for y with respect to t, put y(t)
for y with respect to x, leave it as y

#How to run

install matplotlib
file name: Differential Equations Calculator (DEC)

#How it works
1. DEC reads the equations and finds its order ( does not tell user the order)
2. Solves the ODE with Sympy's 'dsolve'
3. Takes in user input for the initial conditions
4. Dec Plots the particular solution with matplotlib

#limitations
1. Suports first and second order differntial equations

#Coming Updates
1. DEC will tell you the order of the ODE given
2. DEC will not soon run partial differential equations
