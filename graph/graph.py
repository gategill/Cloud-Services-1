import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os



def input_fn(file):
    f = r'C:\Users\Asus\Desktop\Cloud-Services'
    f += "\\" + file 
    
    H_wsl = pd.read_csv(f, sep = ',', header = None, skiprows = 1, na_filter = False, squeeze = True, dtype = np.float64, float_precision = 'high')

    int_wsl_total = H_wsl.iloc[0]
    int_wsl_total5 = H_wsl.iloc[2]

    mat_wsl_total = H_wsl.iloc[4]
    mat_wsl_total5 = H_wsl.iloc[6]

    sym_wsl_total = H_wsl.iloc[8]
    sym_wsl_total5 = H_wsl.iloc[10]

    total_wsl_sim = H_wsl.iloc[12]

    integrate_wsl = H_wsl.iloc[14:263] # 263]

    matrix_wsl = H_wsl.iloc[264:513] # 264:513]

    sym_wsl = H_wsl.iloc[514:]


    return integrate_wsl, matrix_wsl, sym_wsl





def plot_single(file, chart_name):
    Integrate, Matrix, Sympy = input_fn(file)
    for i in [(Integrate,"Numpy Integral"),(Matrix,"Matrix Multiplication"),(Sympy,"Sympy Integral")]:
        t = np.arange(1,499,2)
        plotter(t,i[0].T,i[1],chart_name)
    return (Integrate,Matrix,Sympy)


def plot_multi(h,v,d):
    t = np.arange(1,499,2)

    multi_plotter(t,h[0],v[0],d[0],'Numpy Integrate')
    multi_plotter(t,h[1],v[1],d[1], 'Matrix Multiplication')
    multi_plotter(t,h[2],v[2],d[2], 'Sympy Integrate')


def multi_plotter(t,h,v,d,name):
    fig, ax = plt.subplots()
    
    ax.plot(t, h, color='tab:blue', label = 'Host')
    
    ax.plot(t, v, color='tab:orange', label = 'VM')
    
    ax.plot(t, d, color='tab:green', label = 'Docker')

    ax.set(xlabel='Size of input (n)', ylabel='Execution time (s)',
            title= name + ' Function on All')
    ax.grid()
    ax.legend()

    fig.savefig(name+".png")
    plt.show()


def plotter(t,s,name,chart_name):
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='Size of input (n)', ylabel='Execution time (s)',
            title= name + ' Function on ' + chart_name)
    ax.grid()

    fig.savefig(name+chart_name+".png")
    plt.show()


def plot(host,vm,docker):
    names = ('Host','VM','Docker')
    h = plot_single(host,names[0])
    v = plot_single(vm,names[1])
    d = plot_single(docker, names[2])
    plot_multi(h,v,d)


if __name__ == '__main__':
    plot('host_final.txt','vm_final.txt','docker_final.txt')

