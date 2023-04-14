import matplotlib.pyplot as plt
import numpy as np

try:
    data = np.loadtxt('Lab4/graphic.txt')
    x = data[:,0]
    y = data[:,1]
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("График функции")
    plt.savefig('Lab4/График.svg')
    plt.show()

except FileNotFoundError:

    function_str = input("Введите выражение для функции: ")
    x_min = float(input("Введите минимальное значение аргумента: "))
    x_max = float(input("Введите максимальное значение аргумента: "))
    step = float(input("Введите шаг вычисления: "))
    x = np.arange(x_min, x_max, step)
    y = eval(function_str)

    
    with open('Lab4/graphic.txt', 'w') as f:
        for i in range(len(x)):
            f.write(f"{x[i]:.6f} {y[i]:.6f}\n")

    
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("График функции")
    plt.savefig('Lab4/График.svg')
    plt.show()
#Готовый график