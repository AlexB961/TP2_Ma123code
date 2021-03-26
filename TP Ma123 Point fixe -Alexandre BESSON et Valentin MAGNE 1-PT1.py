"""
TP Ma123 - point fixe - M.Laurent Bletzacker

Alexandre Jean-Philippe BESSON
Valentin MAGNE
1-PT (1)

"""

import math

def PointFixe(g,x0,epsilon,Nitermax):
    n = 0
    xold = x0
    erreur = g(xold) - xold
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        n += 1
        print(n, xnew)
    return xnew

#(fonction):x**4 + 3x = 9

def g1(x):
    return ((9 - 3*x) ** (1/4))

print("POUR f1 nous aurons:", PointFixe(g1,1.5,1e-3,5e4))

#(fonction):x = 3cos(x)-2

def g2(x):
    return (math.acos((x+2)/3))

print("POUR f2 nous aurons:", PointFixe(g2,0.55,1e-3,5e4))

#(fonction):x*e^x = 7

def g3(x) :
    return ((math.log(7/x)))

print("POUR f3 nous aurons:", PointFixe(g3,1.5,1e-3,5e4))

#(fonction): e^x − x = 10

def g4(x):
    return ((math.log(10+x)))
print("POUR f4 nous aurons:", PointFixe(g4,2.5,1e-3,5e4))

#(fonction): 2tan(x) = x + 5

def g5(x):
    return (math.atan((x+5)/2))
print("POUR f5 nous aurons:", PointFixe(g5,1.5,1e-3,5e4))

#(fonction):e^x = x^2 + 3

def g6(x):
    return((math.log(x**2 +3)))
print("POUR f6 nous aurons:", PointFixe(g6,1.4,1e-3,5e4))

#(fonction):3x + 4 ln(x) = 7

def g7(x):
    return((7-4*math.log(x))/3)
print("POUR f7 nous aurons:", PointFixe(g7,1.7,1e-3,5e4))

#(fonction):x^4 − 2x^2 + 4x = 17

def g8(x):
    return((2*(x**2)-4*x +17)**(0.25))
print("POUR f8 nous aurons:", PointFixe(g8,2,1e-3,5e4))

#(fonction):e^x -2sin(x) =7

def g9(x):
    return(math.log(7+(2*math.sin(x))))
print("POUR f9 nous aurons:", PointFixe(g9,2.5,1e-3,5e4))

#(fonciton): ln(x^2+4)*e^x =10 

def g10(x):
    return(math.log(10) - math.log(math.log(x ** 2 + 4)))
print("POUR f10 nous aurons:", PointFixe(g10,1.5,1e-3,5e4))

