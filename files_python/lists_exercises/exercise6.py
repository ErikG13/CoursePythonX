def maxNumberList():
    try:
        list_n = []
        while True:
            n = input("Ingrese un número:> ")
            if n != 'hecho':
                list_n.append(int(n))
            else:
                print(max(list_n))
                break
    except ValueError:
        print("No es un numero")

maxNumberList()