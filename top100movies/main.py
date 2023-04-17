import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
top_movies = soup.findAll(name="h3", class_="title")
top_movie_list = [movie.text for movie in reversed(top_movies)]

print(top_movie_list)
#

with open("movies.txt", "w") as file:
    for movie in reversed(top_movies):
        file.write(f"{movie.text}\n")

