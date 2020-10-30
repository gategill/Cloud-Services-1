import numpy as np

def integrate_boole(f,lr,N):
    (l,r) = lr 
    N = 4*int(N//4)
    h = (r-l)/N
    xN = np.linspace(l,r,N+1)
    fN = f(xN)
    return (2*h/45)*(7*fN[0]+32*np.sum(fN[1:-1:2])+12*np.sum(fN[2:-2:4])+14*np.sum(fN[4:-4:4])+7*fN[-1])


if __name__ == "__main__":
    sine_int= integrate_boole(lambda x: np.sin(x), lr = (0,np.pi), N = 8)
    print(sine_int)
