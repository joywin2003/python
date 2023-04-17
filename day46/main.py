# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# timeline = input("which year you would like to travel to in YYY-MM-DD:")
#
# LINK =f"https://www.billboard.com/charts/hot-100/{timeline}/"
#
# response = requests.get(LINK)
# data = response.text
#
# soup = BeautifulSoup(data,"html.parser")
# top_songs = soup.findAll(name="h3",class_="c-title")
# list = [songs.getText().strip() for songs in top_songs]
# print(list)
#
#
# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id="bab57477e0d34e6baa6049d8f70e9a76",
#     client_secret="96a85b542aeb44c5995460704fd79d42",
#     redirect_uri=" https://example.com",
#     scope="playlist-modify-private"))
# user_id = spotify.current_user()["id"]


import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="bab57477e0d34e6baa6049d8f70e9a76"
CLIENT_SECRET ="96a85b542aeb44c5995460704fd79d42"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]