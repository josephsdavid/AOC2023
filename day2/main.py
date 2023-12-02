import os
import sys
from functools import reduce

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from utils.time_run import log_time

pwd = os.path.dirname(os.path.abspath(__file__))


def load_data(fp):
    with open(f"{pwd}/{fp}", 'r') as f:
        data = f.read().splitlines()
        arr = [x if x != "" else "" for x in data]
        return arr


def game_id(game):
    return int(game.split(":")[0].split(" ")[1])


def parse_game(game):
    game = game.split(": ")[1]
    rounds = game.split("; ")
    d = dict()
    for r in rounds:
        plays = r.split(", ")
        for p in plays:
            rs = p.split(" ")
            bucket = rs[1]
            value = int(rs[0])
            if bucket not in d.keys():
                d[bucket] = value
            else:
                d[bucket] = max(value, d[bucket])
    return d


@log_time
def run_part_A():
    data = load_data("input.txt")
    possible = {"red": 12, "green": 13, "blue": 14}
    possible_games = []
    for row in data:
        scores = parse_game(row)
        is_possible = True
        for k in possible.keys():
            if k not in scores.keys():
                continue
            if possible[k] < scores[k]:
                is_possible = False
                break
        if is_possible:
            possible_games.append(game_id(row))
    return sum(possible_games)


@log_time
def run_part_B():
    data = load_data("input.txt")
    powers = []
    for row in data:
        scores = parse_game(row)
        prod = []
        for k in ["red", "green", "blue"]:
            if k in scores.keys():
                prod.append(scores[k])
        powers.append(reduce(lambda x, y: x*y, prod))
    return sum(powers)


print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")
