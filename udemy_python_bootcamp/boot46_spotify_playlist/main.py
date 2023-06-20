import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# imrpove by creating a project layout

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

timetravel_to = "1991-01-03"
billboard_url = "https://www.billboard.com/charts/hot-100/"+timetravel_to

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

# improve by combining artist and song, instead of year and song?
# imrpove by looking for a similar song name if song does not exist?
song_uris = []
year = timetravel_to.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{timetravel_to} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
