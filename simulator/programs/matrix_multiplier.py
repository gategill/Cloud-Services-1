import numpy as np
import time

def gen_matrix(n):
    matrix_1 = np.random.rand(n,n)
    matrix_2 = np.random.rand(n,n)
    return np.dot(matrix_1,matrix_2)

if __name__ == '__main__':
    print('matrix')
    for i in range(1,500,2):
        tic = time.time()
        gen_matrix(i)
        toc = time.time()
        print(toc-tic)
    print("####")