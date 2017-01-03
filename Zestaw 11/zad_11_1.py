import random
import math


#rozne liczby od 0 do N-1 w kolejnosci losowej
def random_list(n):
    random_l = list(range(n))
    random.shuffle(random_l)
    return random_l


#rozne liczby od 0 do N-1 prawie posortowane (liczby sa blisko swojej prawidlowej pozycji)
def nearly_sorted_list(n):

    nearly_sorted = list(range(n))

    for i in range(n):

        distance = round(math.log(random.randint(1, n/3)))

        if distance == 0:
            while distance != 0:
                distance = round(math.log(random.randint(1, n/3)))

        if i-distance < 0:
            a = 0
        elif i+distance >= n:
            a = n-1
        else:
            a = int(i+distance)

            nearly_sorted[i], nearly_sorted[a] = nearly_sorted[a], nearly_sorted[i]

    return nearly_sorted


#rozne liczby od 0 do N-1 prawie posortowane w odwrotnej kolejnosci
def reversed_nearly_sorted_list(n):
    nearly_sorted = nearly_sorted_list(n)
    return nearly_sorted[::-1]


#N liczb w kolejnosci losowej o rozkladzie gaussowskim
def gaussian_discrete_list(n):
    return [round(random.gauss(n, n/3)) for _ in range(n)]


#N liczb w kolejnosci losowej, o wartosciach powtarzajacych sie, nalezacych do zbioru k elementowego (k < N, np. k*k = N)
def repeated_elements_list(n):
    return [random.randint(0, math.floor(math.sqrt(n))) for _ in range(n)]
