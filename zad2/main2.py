def NOD(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


if __name__ == '__main__':
    a = 100
    b = 10

    result = NOD(a, b)

    print(f"НОД({a}, {b}) = {result}")
