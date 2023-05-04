while True:
    opcion = input("operracion a realizar")
    n1 = int( input("introduce tu primer numero"))
    n2 = int( input('introduce el segundo numer'))

    if opcion =='suma':
        print(n1 + n2)
    elif opcion == 'resta':
        print(n1 - n2)
    elif opcion == 'division':
        print(n1 / n2)
    elif opcion == 'multiplicacion':
        print(n1 * n2)
    else:
        print('no se encontrola opcion')
        break
