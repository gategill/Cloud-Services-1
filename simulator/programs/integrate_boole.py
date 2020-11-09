import numpy as np
import time

def integrate_boole(f,lr,N):
    (l,r) = lr 
    N = 4*int(N//4)
    h = (r-l)/N
    xN = np.linspace(l,r,N+1)
    fN = f(xN)
    return (2*h/45)*(7*fN[0]+32*np.sum(fN[1:-1:2])+12*np.sum(fN[2:-2:4])+14*np.sum(fN[4:-4:4])+7*fN[-1])


if __name__ == "__main__":
    for n in [1,2,5,10,50,100,500]:
        integrate_boole(lambda x: np.exp(x), lr = (0,n), N = 8)