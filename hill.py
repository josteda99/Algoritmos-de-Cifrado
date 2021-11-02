import string
import numpy as np

abc = list(string.ascii_lowercase)


def cifrar(men, key):
    val = []
    menNum = []
    menEnc = []
    men = men.replace(' ', '')
    menNum = convertirMensajeNumero(menNum, men)
    val = multiplicarVecKey(men, val, key, menNum)
    menEncr = traducirALetras(val, menEnc)
    print(menEncr)


def descifrar(men, key):
    val = []
    menNum = []
    menEnc = []
    men = men.replace(' ', '')
    menNum = convertirMensajeNumero(menNum, men)
    key = inversaMatriz(key)
    val = multiplicarVecKey(men, val, key, menNum)
    menEncr = traducirALetras(val, menEnc)
    print(menEncr)


def convertirMensajeNumero(menNum, men):
    for i in range(len(men)):
        for j in range(len(abc)):
            if(men[i] == abc[j]):
                menNum.append(j)

    if len(menNum) % 2 != 0:
        menNum.append(0)
    return menNum


def multiplicarVecKey(men, val, key, menNum):
    for i in range(0, len(men), 2):
        temp = []
        temp.append(menNum[i])
        temp.append(menNum[i+1])
        val.append(np.dot(temp, key) % 26)
    return val


def traducirALetras(val, menEnc):
    for i in range(len(val)):
        menEnc.append(abc[val[i][0]])
        menEnc.append(abc[val[i][1]])
    menEncr = "".join(menEnc)
    return menEncr


def inversaMatriz(key):
    matrizAdj = [[key[1][1], -key[0][1]],
                 [-key[1][0], key[0][0]]]
    determinante = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
    determinante, r, c = gcd(determinante, 26)
    inversa = np.array(matrizAdj) * determinante
    for i in range(2):
        for j in range(2):
            inversa[i][j] = inversa[i][j] % 26
    return inversa


def gcd(a, b):
    # sacado de jutsyusblog
    if b == 0:
        return 0, 1, 0

    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1

        a = b
        b = r

        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return a, u0, v0


def tieneInversa(key):
    condicion1 = False
    condicion2 = False
    matrizAdj = [[key[1][1], -key[0][1]],
                 [-key[1][0], key[0][0]]]
    determinante = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26
    if determinante == 1:
        condicion1 = True

    temp, r, c = gcd(determinante, 26)
    if temp == 1:
        condicion2 = True

    if condicion1 == True and condicion2 == True:
        return True
    else:
        return False


if __name__ == '__main__':
    print('hola, introduzca la clave invertible de 2x2')
    matriz = [[0, 0], [0, 0]]
    matriz[0][0] = int(input('introduzca 0,0: '))
    matriz[0][1] = int(input('introduzca 0,1: '))
    matriz[1][0] = int(input('introduzca 1,0: '))
    matriz[1][1] = int(input('introduzca 1,1: '))

    while(tieneInversa(matriz) != True):
        print('intentelo de nuevo')
        matriz[0][0] = int(input('introduzca 0,0: '))
        matriz[0][1] = int(input('introduzca 0,1: '))
        matriz[1][0] = int(input('introduzca 1,0: '))
        matriz[1][1] = int(input('introduzca 1,1: '))
        tieneInversa(matriz)

    print('Escoja una opcion:')
    print('1: cifrar')
    print('2: descifrar')
    print('cualquier otra para salir')
    opt = int(input())
    if opt == 1:
        print('Introduzca el mensaje a cifrar (minusculas)')
        mensaje = input()
        cifrar(mensaje, matriz)
    elif opt == 2:
        print('Introduzca el mensaje a descifrar (minusculas)')
        mensaje2 = input()
        descifrar(mensaje2, matriz)
    else:
        print('la opcion no existe')
