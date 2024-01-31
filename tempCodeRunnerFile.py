from botasaurus import bt

from src import Gmaps

#love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = [
   "Stone Companies in Kota"
]

Gmaps.places(queries, max=5)