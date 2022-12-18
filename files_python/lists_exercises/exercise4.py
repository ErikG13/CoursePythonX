def find_words(path = ''):
    try:
        f = open(path)
        list_words =[]
        for raw in f:
            words = list(raw.split(' '))
            for word in words:
                if word not in list_words:
                    list_words.append(word.rstrip())
        print(list_words)
    except Exception as e:
        print("Error: {}".format(e))
    
    

find_words('./files_python/lists_exercises/romeo.txt')