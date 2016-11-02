#!/usr/bin/python


def factorial(n):
    product = 1

    for i in range(1, n+1):
        product *= i

    return product


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0
    prev = 1
    result = 0

    # zapis w range oczywiscie mozna uproscic, jednakze pozostawiam go w tej formie dla zwiekszenia czytelnosci
    for i in range(2, n+1):
        result = prev + prev2
        prev2 = prev
        prev = result

    return result
