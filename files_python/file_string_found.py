def ejercicio1():
    try:
        f = open('./files_python/mbox-short.txt')
        for line in f:
            print(line, end='')
    except Exception as e:
        print(e)

def ejercicio2():
    try:
        #f = open('./files_python/mbox-short.txt')
        f = open('./files_python/mbox.txt')
        spam_prom = 0
        row_count = 0
        for row in f:
            row = row.rstrip()
            if row.startswith('X-DSPAM-Confidence'):
                spam_prom = spam_prom + float(row[row.index('0'):])
                row_count += 1
        print("Promedio {}".format(spam_prom/row_count))
    except Exception as e:
        print(e)

def ejercicio3():
    try:
        file = input('Ingrese el nombre del archivo> ')
        f = open('./files_python/{}'.format(file))
        count = 0
        for line in f:
            if line.startswith('Subject'):
                count += 1
        print("Hay {} lineas subject en {}".format(count,file))
    except FileNotFoundError:
        print("No se puede leer el archivo: {}".format(file))

ejercicio3()