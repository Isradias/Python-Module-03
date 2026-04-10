import random

achievement_list = [
    'Crafting Genius',
    'Strategist',
    'World Savior',
    'Speed Runner',
    'Survivor',
    'Master Explorer',
    'Treasure Hunter',
    'Unstoppable',
    'First Steps',
    'Collector Supreme',
    'Untouchable',
    'Sharp Mind',
    'Boss Slayer'
]

players = [
    'Alice',
    'Bob',
    'Charlie',
    'Dylan',
    'Jake',
    'Israel'
]

class Player_class():
    def __init__(self, name):
        self.name = name
        self.achievements = self.gen_player_achievement()
        self.unique = set()
        self.missing = set()

    def gen_player_achievement(self):
        nb_achievements = random.randint(1, 7)
        return set(random.sample(achievement_list, nb_achievements))


if (__name__ == "__main__"):
    nb_players = random.randint(4, 6)
    players_list = random.sample(players, nb_players)
    players_object = [Player_class(name) for name in players_list]
    common_achievements = set.intersection(
                        *(p.achievements for p in players_object))

    for p1 in players_object:
        others = set.union(
                *(p2.achievements for p2 in players_object if p1 != p2))
        p1.unique = set.difference(p1.achievements, others)

    for p in players_object:
        p.missing = set.difference(set(achievement_list), p.achievements)
 
    print("=== Achievement Tracker System ===\n")
    for player in players_object:
        print(f"Player: {player.name}: {player.achievements}")
    
    print(f"\nAll distinct achievements: {set(achievement_list)}\n")

    print(f"Common achivements: {common_achievements}\n")
    for player in players_object:
        print(f"Only {player.name} has: {player.unique}")

    print("")

    for player in players_object:
        print(f"{player.name} is missing: {player.missing}")
