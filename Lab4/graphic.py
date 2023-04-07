import numpy as np
import matplotlib.pyplot as plt

# Запрос параметров функции
function_str = input("Введите функцию: ")
x_min = float(input("Введите минимальное значение x: "))
x_max = float(input("Введите максимальное значение x: "))
step = float(input("Введите шаг вычисления: "))

# Создание массива x
x = np.arange(x_min, x_max + step, step)

# Вычисление значений функции
y = eval(function_str)

# Сохранение результатов в файл
with open("Lab4/result4.txt", "w") as file:
    for i in range(len(x)):
        file.write("{},{}\n".format(x[i], y[i]))

# Построение графика
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции")
plt.savefig('Lab4/график.svg', format='svg')
plt.show()



# Проверка наличия файла с данными
try:
    with open("Lab4/result4.txt", "r") as file:
        data = file.read()
    print("Данные из файла:")
    print(data)
except FileNotFoundError:
    pass

