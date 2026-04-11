import random

inicial = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam'
]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    print(f"Inicial list of players: {inicial}\n")
    capitalized = [name.capitalize() for name in inicial]
    print(f"New list with all names capitalized: {capitalized}\n")
    already = [name for name in inicial if name == name.capitalize()]
    print(f"New list capitalized names only: {already}\n")
    score_list = {name: random.randint(0, 1001) for name in capitalized}
    print(f"Score dict: {score_list}\n")
    average = sum(score_list[name] for name in score_list) / len(score_list)
    average = round(average, 2)
    print(f"Score average is {average}\n")
    high = {n: score_list[n] for n in score_list if score_list[n] > average}
    print(f"High scores: {high}")
