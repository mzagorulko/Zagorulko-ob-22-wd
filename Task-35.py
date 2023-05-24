def fibonacci_sequence(terms):
    n1, n2 = 0, 1

    if terms == 1:
        return [n1]
    else:
        result = [n1, n2]
        for i in range(2, terms):
            result.append(result[i - 2] + result[i - 1])
        return result


print(fibonacci_sequence(int(input("Введите желаемое колмчество чисел последовательности Фибоначчи: "))))
