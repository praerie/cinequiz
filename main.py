from bs4 import BeautifulSoup
import requests
from util import get_title, get_year, get_director
from quiz import game_round, interpret_round
import const as c


page = requests.get(f"{c.domain}{c.directory}")
soup = BeautifulSoup(page.text, "html.parser")

films = soup.find("tbody", class_="lister-list").find_all("tr")
film_data = []

for film in films:
    film_data.append({"title": get_title(film),
                      "year": get_year(film),
                      "director": get_director(film)})

print(f"Welcome to {c.game_title}!\n"
      f"To make your guess, please enter the digit associated with your answer.\n")

round_count = 0
points = 0

while round_count < c.round_max:
    round_count += 1

    outcome = game_round(film_data, "director", "title", c.director_question)     # guessing director of title
    points = interpret_round(outcome, points)

    outcome = game_round(film_data, "year", "title", c.year_question)             # guessing year of title
    points = interpret_round(outcome, points)

    outcome = game_round(film_data, "title", "director", c.title_question)        # guessing title of director
    points = interpret_round(outcome, points)

print(f"You answered {points} out of {c.round_max * 3} correctly.\n"
      f"Thank you for playing {c.game_title}!\n")
