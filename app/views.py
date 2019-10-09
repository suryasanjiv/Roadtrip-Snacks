# views.py

from flask import render_template, redirect
from app import app
from app import credentials
from urllib import parse

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/auth', methods = ['GET'])
def gen_playlist():
    client_id = credentials.client_id
    client_secret = credentials.client_secret
    redirect_uri = credentials.redirect_uri
    #credentials.getSpotifyInstance

    # return credentials.promptUser(credentials.client_id, credentials.client_secret, credentials.redirect_uri)
    # return redirect("https://accounts.spotify.com/en/authorize?client_id=%s&response_type=code&scope=%s&redirect_uri=%s" % (client_id, parse.quote_plus(credentials.SCOPE), parse.quote_plus(redirect_uri))))
    # return credentials.promptUser(credentials.client_id, credentials.client_secret, credentials.redirect_uri)

    return redirect(credentials.promptUser(credentials.client_id, credentials.client_secret, credentials.redirect_uri))
