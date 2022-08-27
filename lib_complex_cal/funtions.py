import math

# ------metodos para mejorar la interfas de usuario------


def prettyCpx(numCpx):
    part_R, part_i = numCpx
    if(part_i < 0):
        return f"({part_R} - {abs(part_i)}i)"
    return f"({part_R} + {part_i}i)"


def polarWriter(angulo, modulo):
    return f"{format(modulo, '2f')}e^({format(angulo, '2f')}i)"

# ------metodos para mejorar la interfas de usuario------


def sumaCpx(a: complex, b: complex, raw=None) -> complex:
    """Recibe dos nuemros complejos a, b y los suma"""
    result = ((a[0] + b[0]), (a[1] + b[1]))
    if(raw == None):
        return prettyCpx(result)
    return result


def restaCpx(a: complex, b: complex, raw=None) -> complex:
    """Recibe dos nuemros complejos a, b y le resta b a a"""
    result = ((a[0] - b[0]), (a[1] - b[1]))
    if(raw == None):
        return prettyCpx(result)
    return result


def productoCpx(a: complex, b: complex, raw=None) -> complex:
    """Realiza el producto de dos numeros complejos a y b"""
    result = (((a[0] * b[0]) - (a[1]) * b[1]), (a[0] * b[1] + a[1] * b[0]))
    if(raw == None):
        return prettyCpx(result)
    return result


def divisionCpx(num: complex, den: complex, raw=None) -> complex:
    """Divide dos números complejos num y den, num/den"""
    conjDen = conjugadoCpx(den, 1)
    if (productoCpx(den, conjDen, 1)[0] == 0):
        return "El denominador no puede ser zero, prueba otro número :)"
    denxConj = 1/productoCpx(den, conjDen, 1)[0]
    numxConj = productoCpx((conjDen), num, 1)
    result = tuple(map((lambda x: x*denxConj), numxConj))
    if(raw == None):
        return prettyCpx(result)
    return result


def moduloCpx(a: complex) -> float:
    """retorna el modulo de un número complejo"""
    aCuadrado = list(map((lambda x: x*x), a))
    return (aCuadrado[0] + aCuadrado[1])**(1/2)


def conjugadoCpx(a: complex, raw=None) -> complex:
    """retorna el conjugado de un número complejo a"""
    conjugado = list(a)
    conjugado[1] = -conjugado[1]
    if(raw == None):
        return prettyCpx(conjugado)
    return conjugado


def polarToCart(modulo: float, angulo: float, raw=None) -> complex:
    """recibe el modulo y el angulo de un número complejo, y lo devuelve
    en su forma cartesiana"""
    angulo = math.radians(angulo)
    result = (modulo * math.cos(angulo), modulo * math.sin(angulo))
    if(raw == None):
        return prettyCpx(result)
    return result


def cartToPolar(a: complex) -> complex:
    """recibe un número complejo y lo devueve en su forma polar |m|*e^(angulo*i)"""
    moduloNum = moduloCpx(a)
    angulo = faseCpx(a)
    print(angulo)
    print(polarWriter(angulo, moduloNum))
    return (moduloNum * (math.cos(angulo)), moduloNum * (math.sin(angulo)))


def faseCpx(a):
    """retorna la fase de un complejo"""
    return ((math.atan2(a[1], a[0])) * 180 / math.pi)
