import numpy
import numpy as np
try:
    file1 = open("Lab3/data/app.conf", "r")
    try:
        spisok = file1.readlines()
        celchisl = []
        arr1 = []
        print(spisok)
        for i in spisok:
            for j in i:
                if j == " ":
                    continue
                else:
                    celchisl.append(j)

        celchisl = list(map(int, celchisl))
        arr = numpy.array(celchisl)
        element = arr[0]
        arr = np.delete(arr, 0)
        arr1.append(element)
        print(arr1)
        print(arr)
        
        

        newres = []
        i = 0
        while i < element:
            i = i + 1
            newres.append(arr[0]*i + arr[1])
        print(newres)
    finally:
        file1.close()

    with open("Lab3/data/result.dat", "w") as file23:
        file23.write(str(newres))
        file23.close()

except FileNotFoundError:
    print("Невозможно открыть файл")
    newfile = open("Lab3/data/app.conf", "w")
    newfile.write(input("Введите числа a b c через пробел"))
    newfile.close()
    newfile = open("Lab3/data/app.conf", "r")
    spisok = newfile.readlines()
    celchisl = []
    arr1 = []
    print(spisok)
    for i in spisok:
        for j in i:
            if j == " ":
                continue
            else:
                celchisl.append(j)

        celchisl = list(map(int, celchisl))
        arr = numpy.array(celchisl)
        element = arr[0]
        arr = np.delete(arr, 0)
        arr1.append(element)
        print(arr1)
        print(arr)

        newres = []
        i = 0
        while i < element:
            newres.append(arr[0]*i + arr[1])
            i = i + 1
    newfile.close()
    with open("Lab3/data/result.dat","w+") as file24:
        file24.write(str(newres))
        file24.close()
        
    
except:
    print("Ошибка при работе с файлом")

#Готовая лабораторная