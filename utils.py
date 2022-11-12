# country_dict = {'Rank': '33', 'CCA3': 'ARG', 'Country/Territory': 'Argentina', 'Capital': 'Buenos Aires', 'Continent': 'South America', 
# '2022 Population': '45510318', '2020 Population': '45036032', '2015 Population': '43257065', '2010 Population': '41100123', '2000 Population': '37070774', '1990 Population': '32637657', '1980 Population': '28024803', '1970 Population': '23842803', 'Area (kmÂ²)': '2780400', 'Density (per kmÂ²)': '16.3683', 'Growth Rate': '1.0052', 'World Population Percentage': 
# '0.57'}

def get_population(country_dict):   # funcion que retorna un array con los años y uno con los valores de poblacion

    # creo un diccionario con los años y su poblacion

    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }

    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values


# funcion para seleccionar el diccionario del pais
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))  # cada item de la lista es  un diccionario, busco extraer solo el diccionario del pais que ingreso, y lo transformo en una lista con un solo item que es el diccionario del pais que quiero
  return result