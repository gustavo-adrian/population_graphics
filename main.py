import read_csv
import utils
import charts


def run():
    data = read_csv.read_csv('./data.csv')   # traigo la data entera

    # cada item de data es un diccionario
    continent =  list(filter(lambda item: item['Continent'] == 'North America', data ))
    # data es una lista de diccionarios, 
    # de cada diccionario por clave creo una lista con los nombres de los paises
    countries = list(map(lambda country: country['Country/Territory'], continent))  #country es un diccionario
    # creo una lista con los porcentages de poblacion 
    percentages = list(map(lambda country: country['World Population Percentage'], continent))    
    # tengo ahora dos lista de igual tamaños para hacer un graficos de torta

    charts.generate_pie_chart(countries, percentages)

    country = input('Ingrese pais: ')   # pido seleccionar un pais
    result = utils.population_by_country(data, country) # traigo el la lista con el diccionario del pais ingresado

    if len(result) > 0: # la lista result tiene que tener un elemento que es el diccionario
        country = result[0]   # aca solo tengo el diccionario
        labels, values = utils.get_population(country)

        charts.generate_bar_chart(country['Country/Territory'],labels, values)


if __name__ == '__main__':
    run()

    