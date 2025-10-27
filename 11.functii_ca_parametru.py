

def patrat(x):
    return x ** 2

def cub(x):
    return x ** 3

def calculeaza(functie, x):
    return functie(x)

## Programare functionala
print(calculeaza(patrat, 5))

print(calculeaza(cub, 3))