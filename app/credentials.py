import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import os, sys

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret,redirect_uri)

print(client_id)
print(client_secret)
print(redirect_uri)

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

#credentials = oauth2.SpotifyClientCredentials(client_id, client_secret)
# # token = credentials.get_access_token()
# token = util.prompt_for_user_token(username, scope)
# token = util.prompt_for_user_token(username, scope, client_id = 'your-app-redirect-url', client_secret=' your-app-redirect-url', redirect_uri = 'your-app-redirect-url')

# spotify = spotipy.Spotify(auth=token)
