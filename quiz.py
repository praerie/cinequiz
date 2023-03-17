from util import get_options, check_input
import random


def game_round(film_data, target_type, question_type, question):
    target = random.choice(film_data)

    options = get_options(film_data, target, target_type)
    print(f"{question}\n>>> {target[question_type]}")
    print(f"1: {options[0]}\n"
          f"2: {options[1]}\n"
          f"3: {options[2]}")

    attempt = check_input()

    if options[attempt-1] == target[target_type]:
        print("Correct! +1\n")
        return True
    else:
        print(f"Incorrect. Correct answer: {target[target_type]}.\n")
        return False


def interpret_round(outcome, points):
    if outcome:
        points += 1
        return points
    else:
        return points
