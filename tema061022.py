import random

n1 = random.randint(2, 99)
n2 = random.randint(2, 99)
b = random.randint(2, 9)


def baza_numerelor(x, b):
    if (b > 1) and (b < 10):
        for i in [j for j in str(x)]:
            if int(i) < b:
                return True
            else:
                return False
    else:
        return False

print(baza_numerelor(n1, b))

def suma_numerelor(n1, n2, b):
    if (baza_numerelor(n1, b) == True) and (baza_numerelor(n2, b)) == True:
        suma = n1 + n2
        return suma
    else:
        return "Numarul este scris gresit cu baza " + str(b)

print(suma_numerelor(n1, n2, b))

def diferenta_numerelor(n1, n2, b):
    if (baza_numerelor(n1, b) == True) and (baza_numerelor(n2, b)) == True:
        diferenta = n1 - n2
        return diferenta
    else:
        return "Numarul este scris gresit cu baza " + str(b)


print(diferenta_numerelor(n1, n2, b))


def produsul_numerelor(n1, n2, b):
    if (baza_numerelor(n1, b) == True) and (baza_numerelor(n2, b)) == True:
        produsul = n1 * n2
        return produsul
    else:
        return "Numarul este scris gresit cu baza " + str(b)


print(produsul_numerelor(n1, n2, b))
