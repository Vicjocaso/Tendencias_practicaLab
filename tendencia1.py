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
    if n > 1:
        return fibona(n-1) + fibona(n-2)
    return n

# Funcion par o impar


def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# sepaar


def dig(num):
    return [int(a) for a in str(num)]


# 50 ite
for i in range(50):
    print(fibona(i), primo(i), par_impar(i), dig(i))
