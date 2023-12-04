from utils import InputReader
import re
import math

def get_adjacent_square_coords(idx, x0, x1=None):
    '''Takes the number's start and end index position
    and returns values of all adjacent squares.'''
    if x1:
        coords = [
            (idx - 1, x1),
            (idx, x1),
            (idx + 1, x1),
            (idx - 1, x0 - 1),
            (idx, x0 - 1),
            (idx + 1, x0 - 1)
        ]
        for i in range(x0, x1):
            coords.append((idx + 1, i))
            coords.append((idx - 1, i))

    else:
        coords = [
            (idx - 1, x0 - 1),
            (idx, x0 - 1),
            (idx + 1, x0 - 1),
            (idx - 1, x0),
            (idx + 1, x0),
            (idx - 1, x0 + 1),
            (idx, x0 + 1),
            (idx + 1, x0 + 1),
        ]
    
    # Remove any -1s from the coords
    return [(x, y) for x, y in coords if x != -1 and y != -1]

def get_square(data, x, y):
    return data[x][y]

def get_coord_values(data, coords):
    values = []
    for x, y in coords:
        try:
            values.append(get_square(data, x, y))
        except IndexError:
            continue
    return values

def get_number_from_coordinate(data, x, y):
    if data[x][y] in '0123456789':
        for m in re.finditer('\d+', data[x]):
            if y >= m.span()[0] and y <= m.span()[1]:
                return int(m.group())
            
def get_gear_coords(data):
    for idx, line in enumerate(data):
        for m in re.finditer('\*', line):
            yield (idx, m.span()[0])

def gear_ratios(data):
    for x, y in get_gear_coords(data):
        adjacent_coords = get_adjacent_square_coords(x, y)
        adjacent_numbers = set([get_number_from_coordinate(data, x, y) for x, y in adjacent_coords if get_number_from_coordinate(data, x, y)])
        # This assumes a gear can't be adjacent to two distinct numbers with same value, might not be true for another puzzle
        if len(adjacent_numbers) == 2:
            yield math.prod(adjacent_numbers)
    
def part_numbers(data):
    for idx, line in enumerate(data):
        for m in re.finditer('\d+', line):
            adjacent_square_coords = get_adjacent_square_coords(idx, *m.span())
            if not set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']).issuperset(get_coord_values(data, adjacent_square_coords)):
                yield int(m.group())

def main():
    reader = InputReader(3)
    data = reader.split_lines()
    print(sum(part_numbers(data)))
    print(sum(gear_ratios(data)))

if __name__ == "__main__":
    main()
