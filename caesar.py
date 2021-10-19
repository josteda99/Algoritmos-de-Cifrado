import string


def cifrar(k, men, abc):
    menEnc = []
    for i in range(0, len(men)):
        for j in range(0, len(abc)):
            if men[i] == abc[j]:
                menEnc.append(abc[(j+k) % 26])
    return menEnc


if __name__ == '__main__':
    print('introduzca una opcion:')
    print('1. cifrar')
    print('2. descifrar')
    opt = int(input())
    k = int(input('introduzca key: '))
    men = input('introduzca mensaje: ')

    if opt == 1:
        print(''.join(cifrar(k, men, list(string.ascii_lowercase))))
    elif opt == 2:
        print(''.join(cifrar(k, men, list(string.ascii_lowercase)[::-1])))
    else:
        print('no existe esa opcion')
