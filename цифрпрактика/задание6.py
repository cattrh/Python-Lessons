import math
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, h=1e-5):
        self.h = h

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return lambda x: (instance(x + self.h) - instance(x - self.h)) / (2 * self.h)

class ExponentialFunction:
    derivative = Derivative()  

    def __init__(self, a):
        self.a = a

    def __call__(self, x):
        return self.a * math.exp(x)

    def plot(self):

        x_vals = [x / 10.0 for x in range(-20, 21)]  
        f_vals = [self(x) for x in x_vals]
        df_vals = [self.derivative(x) for x in x_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, f_vals, )
        plt.plot(x_vals, df_vals,)
        plt.show()

exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()