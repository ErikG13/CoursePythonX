def count_FromEmail(path=''):
    try:
        f = open(path)
        cont = 0
        for line in f:
            if line.startswith('From '):
                line = line.split(' ')
                print(line[1])
                cont += 1
        print("Hay {} lineas con 'FROM '".format(cont))
    except Exception as e:
        print(e)
    finally:
        f.close()

count_FromEmail('./files_python/mbox-short.txt')