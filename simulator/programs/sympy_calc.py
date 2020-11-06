from sympy import *

def sympy_integrate(n):
    x = Symbol('x')
    expr = integrate(exp(x),(x,0,n)).evalf()
    return expr
    

if __name__ == '__main__':
    for i in [1,2,5,10,50,100,500]:
        print(sympy_integrate(i))
        