import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) #extrae de la lista la primera fila y ya no forma parte del iterador original
        data = []
        for row in reader:
            iterable = zip(header,row) #se arma una lista, y cada elemento es una tupla de dos valores
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict) #agrego en una lista cada diccionario creado
        return data



