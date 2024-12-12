from matplotlib import pyplot as plt
import os
import numpy as np

dir = os.getcwd()
x = np.linspace(-5, 0, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')

plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.plot(x, [0]*len(x), label='f(x)=0', color='black')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.21, 0.17, 0.50, 0.25])


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 3] = np.nan
    y[y < -3] = np.nan
    return y


x = np.linspace(-5, 0, 1000)
plt.grid()
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='red')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='green')
plt.plot(x, [0]*len(x), label='x=0', color='black')


plt.savefig(dir + '/Занятие_9_3.png', dpi=300)
plt.show()




from matplotlib import pyplot as plt
import os
import numpy as np

dir = os.getcwd()
x = np.linspace(-5, 5, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=0.5), label='a=1,b=0.5', color='red')
plt.plot(x, f(x, a=1, b=-0.5), label='a=1,b=-0.5', color='blue')
plt.plot(x, f(x, a=1, b=-1.5), label='a=1,b=-1.5', color='green')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()
x = np.linspace(-1, 2, 1000)
plt.savefig(dir + '/Занятие_9_4.png', dpi=300)
plt.show()
def example_plot(ax, x, a, b1, b2, array_b, k, fontsize=12, hide_labels=False):
    ax.plot(x, f(x, a, b1), label=f'a={a},b={b1}', color='red')
    ax.plot(x, f(x, a, b2), label=f'a={a},b={b1}', color='blue')
    ax.grid()
    ax.plot(x, f(x, a, array_b[k][0]), label=f'a={a},b={array_b[k][0]}', color='green')
    ax.plot(x, f(x, a, array_b[k][1]), label=f'a={a},b={array_b[k][0]}', color='indianred')
    ax.legend()
    ax.locator_params(nbins=3)
    if hide_labels:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    else:
        ax.set_xlabel('Ось X', fontsize=fontsize)
        ax.set_ylabel('Ось Y', fontsize=fontsize)


fig, axs = plt.subplots(1, 3, figsize=(15, 6))
a = 1
b1 = 0
b2 = -1
array_b = [[0.5, 0.8], [-0.5, -0.8], [-1.5, -2.5]]
k = 0
for ax in axs.flat:
    example_plot(ax, x, a, b1, b2, array_b, k)
    k += 1

plt.savefig(dir + '/Занятие_9_4_2.png', dpi=300)
plt.show()