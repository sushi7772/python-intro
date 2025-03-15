
### ŁACZENIE ZIP 
### DOKUMENTACJA https://docs.python.org/3/library/functions.html#zip

liczby = [1, 2, 3, 4,]

litery = ['a', 'b', 'c', 'd']

polaczone = list(zip(liczby, litery))  

print(polaczone)

### RANDOM
### DOKUMENTACJA https://docs.python.org/3/library/exceptions.html#ValueError

import random


losowa_liczba = random.randint(1, 10)

print(losowa_liczba)
# OBSŁUGA WYJATKU VALUERROR
# DOKUMENTACJA https://docs.python.org/3/library/exceptions.html#ValueError
try:
    wejscie= input("Podaj liczbe")
    liczba = int(wejscie)
    print("podales: ", liczba)
except ValueError:
    print("To nie jest liczba")