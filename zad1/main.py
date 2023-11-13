import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Введите количество элементов:")
    n = int(input())
    massY = [0] * n
    massX = [0] * n

    massY[0] = 1
    massY[1] = 1
    massX[0] = 1
    massX[1] = 2

    i = 2
    while i < n:
        massY[i] = massY[i - 1] + massY[i - 2]
        massX[i] = i + 1
        i += 1

    print(n)
    print(massY)

    plt.plot(massX, massY, marker='o')
    plt.title('Числа Фибоначчи')
    plt.xlabel('Номер числа')
    plt.ylabel('Значение числа')
    plt.grid(True)
    plt.show()
