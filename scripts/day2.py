from utils import InputReader
import re
import math

def get_largest_draws(line: str):
    m = re.match('Game (\d+): (.*)', line)
    game_id = m.group(1)
    draws = [rule.strip() for rule in m.group(2).split(';')]
    largest_draws = {'blue': 0, 'red': 0, 'green': 0}
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            number, color = cube.strip().split()
            if largest_draws[color] < int(number):
                largest_draws[color] = int(number)

    return {game_id: largest_draws}

def possible_games(draws, red_cubes=12, blue_cubes=14, green_cubes=13):
    for draw in draws:
        (game_id, vals), = draw.items()
        if vals['red'] <= red_cubes and vals['green'] <= green_cubes and vals['blue'] <= blue_cubes:
            yield int(game_id)

def part_one(data):
    largest_draws = [get_largest_draws(line) for line in data]
    print(sum(possible_games(largest_draws)))

def get_power(data):
    for line in data:
        (_, largest_draws), = get_largest_draws(line).items()
        yield math.prod(largest_draws.values())

def part_two(data):
    print(sum(get_power(data)))

def main():
    reader = InputReader(2)
    data = reader.split_lines()
    part_one(data)
    part_two(data)

if __name__ == "__main__":
    main()