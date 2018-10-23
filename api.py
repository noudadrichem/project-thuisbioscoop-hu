import requests
import xmltodict
import datetime
from time import strftime
from html import unescape

# date
today = datetime.date.today()
tommorow = today + datetime.timedelta(days=1)
todayFormatted = today.strftime('%d-%m-%Y')
tommorowFormatted = tommorow.strftime('%d-%m-%Y')


def apiRequest(time):
    # api credentials
    uniqueApiId = 'u2urjstlwm7yb4qrkts35wxufnvynim2'
    api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey={}&dag={}&sorteer=0'.format(
        uniqueApiId,
        time 
    )

    # requests response
    r = requests.get(api_url)
    text = r.text
    moviesList = []

    isXML = r.headers['content-type'] == 'text/xml'
    if isXML:
        moviesDic = xmltodict.parse(text)
        for f in moviesDic['filmsoptv']['film']:

            movie = {
                'title': unescape(f['titel']),
                'regiseur' : f['regisseur'],
                'description' : f['synopsis'],
                'imdbScore' : f['imdb_rating'],
                'cast' : f['cast'].split(':'),
                'jaar': f['jaar'],
                'filmduur': f['duur'],
                'start': f['starttijd'],
                'eind': f['eindtijd']
            }

            moviesList.append(movie)

    return moviesList


def movies(time = True):
    if time:
        return apiRequest(todayFormatted) 
    else:
        return apiRequest(tommorowFormatted)

def singleMovie(movieTitle, time = True):
    movies = apiRequest(todayFormatted) if time else apiRequest(tommorowFormatted)

    for movie in movies: 
        if movie['title'] == movieTitle:
            return movie
        else:
            continue
            
