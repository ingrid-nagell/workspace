
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

VAR_PATH = "C:\\Users\\G020772\\repos\\secrets.txt"
with open(VAR_PATH, "r") as f:
    keys = dict(l.strip().split(": ") for l in f)

# Spotify auth
SPOTIFY_CLIENT_ID = keys["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = keys["SPOTIFY_CLIENT_SECRET"]
SPOTIFY_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Spotify api
SPOTIFY_ENDPOINT = f"https://api.spotify.com/v1/users/{user_id}/playlists"

# params = {
#     "name": "python_bootcamp_playlist",
#     "description": f"Top 100 Billboard songs {timetravel_to}",
#     "public": False
# }

# requests.post(SPOTIFY_ENDPOINT, data=params,)


timetravel_to = "1991-01-03"

billboard_url = "https://www.billboard.com/charts/hot-100/"+timetravel_to
print(billboard_url)

response = requests.get(billboard_url)
billboard_top100 = response.text

soup = BeautifulSoup(billboard_top100, 'html.parser')

elements = soup.select("li ul li")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(len(song_names))

artist_names_spans = soup.select("li ul li span")
artist_names = [artist.getText().strip() for artist in artist_names_spans if (artist.getText().strip().isdigit() == False) and (artist.getText().strip() != '-')]
print(len(artist_names))

# artists_and_songs = dict(zip(artist_names, song_names))
# print(artists_and_songs)

song_uris = []
year = timetravel_to.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")