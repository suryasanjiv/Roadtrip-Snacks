# spotify_methods.py

import credentials

sp = credentials.spotify

def get_tarkan_top(sp):
    results = sp.search(q='Tarkan', limit=10)
    for i, t in enumerate(results['tracks']['items']):
        print (' ', i, t['name'])
