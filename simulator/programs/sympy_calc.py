from sympy import *
import time

def sympy_integrate(n):
    
    x = Symbol('x')
    expr = integrate(exp(x),(x,0,n)).evalf()
    return expr
    

if __name__ == '__main__':
    print('sym')
    for i in [1,2,5,10,50,100,500]:
        tic = time.time()
        sympy_integrate(i)
        toc = time.time()
        print(toc-tic)
    print("##")