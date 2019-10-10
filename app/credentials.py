import spotipy
import spotipy.oauth2 as oauth2
import os, sys
from flask import Flask, request

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

def promptUser():
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri)
    url = sp_oauth.get_authorize_url()
    code = sp_oauth.parse_response_code(url)
    sp_oauth.get_access_token(code)
    return url
