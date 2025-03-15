liczby = [1, 2, 3, 4,]

litery = ['a', 'b', 'c', 'd']

polaczone = list(zip(liczby, litery))  

print(polaczone)

import random


losowa_liczba = random.randint(1, 10)

print(losowa_liczba)

try:
    wejscie= input("Podaj liczbe")
    liczba int(wejscie)
    print("podales: ", liczba)
    except ValueError
    print("To nie jest liczba")