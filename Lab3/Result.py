import numpy
try:
    file1 = open("data/app.conf", "r")
    try:
        spisok = file1.readlines()
        celchisl = []
        print(spisok)
        for i in spisok:
            for j in i:
                if j == " ":
                    continue
                else:
                    celchisl.append(j)

        celchisl = list(map(int, celchisl))
        arr = numpy.array(celchisl)
        print(arr)

        newres = []
        i = 0
        while i < arr[0]:
            i = i + 1
            newres.append(arr[1]*i + arr[2])
        print(newres)
    finally:
        file1.close()

    with open("data/result.dat", "w") as file23:
        file23.write(str(newres))
        file23.close()

except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")