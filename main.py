# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
#
# movies_webpage = response.text
# soup = BeautifulSoup(movies_webpage, "html.parser")
# all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles)


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=r'C:\ProgramData\chocolatey\bin\chromedriver.exe')
url = 'https://www.empireonline.com/movies/features/best-movies-2/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

all_movies = soup.find_all("h3")
movie_titles = [movie.getText() for movie in all_movies]
movies = (movie_titles[::-1])

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
