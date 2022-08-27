import math

def prettyCpx(numCpx):
    part_R, part_i = numCpx
    return f"({part_R} + ({part_i}i))"

def polarWriter(angulo, modulo):
    return f"{format(modulo, '2f')}e^({format(angulo, '2f')}i)"    
    

def sumaCpx(a, b):
    result =((a[0] + b[0]), (a[1] + b[1]))    
    return result

def restaCpx(a, b):
    result =((a[0] - b[0]), (a[1] - b[1]))    
    return result
    
def productoCpx(a, b):
    result =(((a[0] * b[0]) - (a[1]) * b[1]), (a[0] * b[1] + a[1] * b[0]))
    return result

def divisionCpx(num, den):    
    conjDen = conjugadoCpx(den)
    denxConj = 1/productoCpx(den, conjDen)[0]
    numxConj = productoCpx((conjDen), num) 
    return list(map((lambda x: x*denxConj), numxConj))

def moduloCpx(a):
    aCuadrado = list(map((lambda x: x*x), a)) 
    return (aCuadrado[0] + aCuadrado[1])**(1/2)

def conjugadoCpx(a):
    conjugado = list(a)
    conjugado[1] = -conjugado[1]
    return conjugado
  
def polarToCart(modulo, angulo):
    angulo = (angulo * math.pi) / 180
    return (modulo * math.cos(angulo), modulo * math.sin(angulo)) 

def cartToPolar(a):
    moduloNum = moduloCpx(a)
    angulo = faseCpx(a)
    print(angulo)
    print(polarWriter(angulo, moduloNum))
    return (moduloNum * (math.cos(angulo)), moduloNum * (math.sin(angulo)))
    

def faseCpx(a):
    return ((math.atan2(a[1], a[0])) * 180 / math.pi)

if __name__ == "__main__":
    a=(-9, -1)
    b=(-7,-1)    
    print(cartToPolar(a))