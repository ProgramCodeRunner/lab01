import matplotlib.pyplot as plt


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print("Введите количество элементов:")
    n = int(input())
    massY = [0] * n
    massX = [0] * n
    for i in range(n):
        massY[i] = fibonacci(i + 1)
        massX[i] = i+1

    print(n)
    print(massY)

    plt.plot(massX, massY, marker='o')
    plt.title('Числа Фибоначчи')
    plt.xlabel('Номер числа')
    plt.ylabel('Значение числа')
    plt.grid(True)
    plt.show()
