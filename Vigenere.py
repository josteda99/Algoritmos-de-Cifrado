import string
import numpy as np

abc = list(string.ascii_lowercase)


def crearMatriz():
    matriz = []
    for i in range(len(abc)):
        a = ['0']*len(abc)
        matriz.append(a)

    for i in range(26):
        aux = i
        for j in range(26):
            matriz[i][j] = abc[aux % 26]
            aux += 1
    return matriz


def cifrar(t, men, cla):
    matriz = crearMatriz()
    men = men.replace(' ', '')
    aux = 0
    for i in range(len(men)):
        cla = cla + cla[aux % len(cla)]
        aux += 1

    indx = indy = 0
    menEnc = []
    for i in range(len(men)):
        for j in range(26):
            if men[i] == abc[j]:
                indx = j

        for k in range(26):
            if cla[i] == abc[k]:
                indy = k
        menEnc.append(matriz[indx][indy])

    menEncr = "".join(menEnc)
    print(menEncr)


def descifrar(t, men, cla):
    matriz = crearMatriz()
    men = men.replace(' ', '')
    aux = 0
    for i in range(len(men)):
        cla = cla + cla[aux % len(cla)]
        aux += 1

    indx = indy = 0
    menEnc = []
    for i in range(len(men)):
        for j in range(26):
            if men[i] == abc[j]:
                indx = j

        for k in range(26):
            if cla[i] == abc[k]:
                indy = k

        menEnc.append(abc[indx-indy])

    menEncr = "".join(menEnc)
    print(menEncr)


if __name__ == '__main__':
    print('Escoja una opcion:')
    print('1: cifrar')
    print('2: descifrar')
    print('cualquier otra para salir')
    opt = int(input())
    if opt == 1:
        print('Introduzca el mensaje a cifrar (minusculas)')
        mensaje = input()
        print('Introduzca la clave (sin espacios)')
        clave = input()
        print('Introduzca t')
        t = input()
        cifrar(t, mensaje, clave)
    elif opt == 2:
        print('Introduzca el mensaje a descifrar (minusculas)')
        mensaje2 = input()
        print('Introduzca la clave (sin espacios)')
        clave2 = input()
        print('Introduzca t')
        t = input()
        descifrar(t, mensaje2, clave2)
    else:
        print('la opcion no existe')
