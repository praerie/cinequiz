import random


def get_director(film):
    try:
        director = film.find("td", class_="titleColumn").a["title"].split(" (")[0]
    except:
        director = "unknown director"

    return director


def get_title(film):
    title = film.find("td", class_="titleColumn").a.text

    return title


def get_year(film):
    try:
        year = film.find("span", class_="secondaryInfo").text.strip("()")
        if len(year) != 4:
            year = "unknown year"
    except:
        year = "unknown year"

    return year


def get_options(film_data, target, film_detail):
    options = [random.choice(film_data)[film_detail],
               random.choice(film_data)[film_detail],
               target[film_detail]]
    shuffled_options = random.sample(options, len(options))

    return shuffled_options


def check_input():
    while True:
        guess = input()

        try:
            guess = int(guess)

            if guess == 1 or guess == 2 or guess == 3:
                return guess
            raise ValueError
        except ValueError:
            print("Error: Please enter the digit associated with your guess.")
