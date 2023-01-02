# recursive function demostration

def Sum(list):

    if len(list) == 0:
        return 0

    return (list[0] + Sum(list[1:]))


def Factorial(value):

    if value == 1:
        return 1

    return value * Factorial(value-1)


print(Sum([1, 2]))
