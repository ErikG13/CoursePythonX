def suma(a, b):
    while True:
        try:
            return a + b
        except TypeError:
            print("Error: No es posible dividir entre cero")
            break