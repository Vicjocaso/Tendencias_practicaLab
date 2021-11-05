# Funcion para saber si un numero es primo o no
def primo(num, n=2):
    if n >= num:
        print("Es primo")
    elif num % n != 0:
        return primo(num, n + 1)
    else:
        print("No es primo")

# Funcion fibonachi


def fibona(n):
    x = []
    a, b = 0, 1
    while a < n:
        print(a + b)
        primo(a)
        print()
        a, b = b, a+b
        x.append(a)
    print(x)


# resultados
fibona(50)
