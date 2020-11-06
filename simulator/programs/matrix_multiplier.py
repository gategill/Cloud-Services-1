import numpy as np

def gen_matrix(n):
    matrix_1 = np.random.rand(n,n)
    matrix_2 = np.random.rand(n,n)
    return np.dot(matrix_1,matrix_2)

if __name__ == '__main__':
    for i in range(2,100):
        gen_matrix(i)