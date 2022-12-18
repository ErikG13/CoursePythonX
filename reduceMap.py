from cmath import e

class Map_fruit:
    input_path = ''
    output_path = ''
    lines_fruit = []
    fruit_list = []

    def __init__(self, input_path='', output_path = ''):
        self.input_path = input_path
        self.output_path = output_path
    
    """
    Funcion que simula el mapeo de archivos del sistema HDFS a traves de MapReduce
    En este ejemplo cada linea de texto es un archivo que contendra informacion
    Que finalmente se guardara en un solo conjunto de informacion, es decir un nodo de archivos (lineas de texto)
    """
    def map_fruit(self): 
        try:
            f = open(self.input_path) #Abre el archivo desde su ruta
            for l in f:
                l = l.rstrip('\n') #Limpia cada linea del texto de los saltos de linea
                self.lines_fruit.append(l) #Agrega cada linea de texto del archivo a una lista
            return self.lines_fruit #Returna la lista
        except Exception:
            print(Exception)
        finally:
            f.close() #Cierra el archivo

    """
    Funcion que simula el agrupamiento de toda la información que existe en el nodo (lista)
    Agrupando cada dato de cada archivo(linea de texto) en el nodo aunque esta se repita en el sistema HDFS(archivo de texto)
    Teniendo como producto final un conjunto de datos de tipo tuplas de clave (data) y valor (1 si es que existe)
    PD: De hecho la finalidad de Reduce es tener la data agrupada en un solo nodo(lista) con el objetivo de reducirla en un
    Solo conjunto con datos no repetidos
    """
    def reduce_fruit(self):
        for token in self.lines_fruit:
            tmp_token = list(token.split(' ')) #Se crea una nueva lista separando cada dato del archivo(linea de texto) por el espacio 
            for tmp in tmp_token:
                self.fruit_list.append(list((tmp,1))) #Se agrega a una nueva lista en forma de tupla(clave,valor)
        return self.fruit_list #Se retorna la nueva lista que contiene todos los datos en forma de tuplas de los archivos (lineas de texto)

    """
    Función que simula el reducir el nodo(Lista que contiene la tupla de toda la informacion del sistema HDFS(Archivo de texto))
    En una sola lista que contendra la información sin duplicidad y ademas el conteo de cada uno de los datos que existian en los archivos (lineas de texto)
    Retornando así el producto final del sistema HDFS
    """
    def reduce_byKey(self):
        dict_tmp = {} #Se crea un diccionario temporal
        for fruta, key in self.fruit_list:
            if fruta in dict_tmp: #Valida si cada clave de la lista se encuentra en el diccionario 
                dict_tmp[fruta] = dict_tmp[fruta] + key #En caso de que exista ya la clave(la información) sumara su valor a la misma clave
            else:
                dict_tmp[fruta] = 1 #En caso contrario se creara la clave (la información) y el valor sera igual a 1
        self.fruit_list = [] #Se vacia la lista anterior
        for key, val in dict_tmp.items():
            self.fruit_list.append([key,val]) #Se agrega la información ya reducida en forma de tupla(clave,valor) eliminando la información duplicada y obteniendo la suma de las veces que la clave(la informacion) se encuentra en el nodo
        return self.fruit_list #Se retorna la lista que contiene el archivo final
    
    """
    Funcion que simula el almacenamiento de la información extraida, cargada y procesada en el sistema hdfs(arcivo de texto)
    """
    def load_data_output(self):
        try:
            f = open(self.output_path, 'w+') #Abre y crea un archivo en caso de no existir
            for key, val in self.fruit_list:
                f.writelines('{} \t {}\n'.format(key,val)) #Escribe cada archivo(tupla) en el sistema HDFS(archivo de texto)
        except Exception as e:
            print(e)
        finally:
            f.close() #Cierra el archivo


mf = Map_fruit("data/input/dfruit_input.txt","data/output/dfruit_output.txt")
mf.map_fruit()
mf.reduce_fruit()
mf.reduce_byKey()
mf.load_data_output()