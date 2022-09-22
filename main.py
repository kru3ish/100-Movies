import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html,'html.parser')
movies = soup.find_all('h3')
movies_title = []
for movie in movies:
    text = movie.get_text()
    movies_title.append(text)

movies = movies_title[::-1]
with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(movie)
        file.write('\n')
