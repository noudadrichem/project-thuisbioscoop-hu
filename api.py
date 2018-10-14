import pprint
import requests
import xmltodict


uniqueApiId = 'u2urjstlwm7yb4qrkts35wxufnvynim2'
api_url =  'http://api.filmtotaal.nl/filmsoptv.xml?apikey=u2urjstlwm7yb4qrkts35wxufnvynim2&dag=14-10-2018&sorteer=0'

r = requests.get(api_url)

text = r.text.encode('ascii', 'ignore')

isXML = r.headers['content-type'] == 'text/xml'
if isXML:
    moviesDic = xmltodict.parse(text)
    for film in moviesDic['filmsoptv']['film']:

        title = film['titel']
        regiseur = film['regisseur']
        description = film['synopsis']
        imdbScore = film['imdb_rating']
        print(title)



def movies():
    return ['een', 'twee', 'drie', 'vier']
