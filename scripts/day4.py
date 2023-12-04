from utils import InputReader
import numpy as np

def parse_line(line: str):
    header, numbers = line.split(':')
    winning_numbers, my_numbers = numbers.split('|')
    winning_numbers = np.array(winning_numbers.split()).astype(int)
    my_numbers = np.array(my_numbers.split()).astype(int)
    return winning_numbers, my_numbers

def get_hit_count(winning_numbers, my_numbers):
    n = len(set(my_numbers).intersection(set(winning_numbers)))
    return n

def score_card(winning_numbers, my_numbers):
    n = get_hit_count(winning_numbers, my_numbers)
    if n > 0:
        return 2**(n - 1)
    else:
        return 0
    
def scores(data):
    for line in data:
        winning_numbers, my_numbers = parse_line(line)
        yield score_card(winning_numbers, my_numbers)

def main():
    data = InputReader(4).split_lines()
    print(sum(scores(data)))
    inventory = {i: 1 for i in range(len(data))}
    for idx, line in enumerate(data):
        winning_numbers, my_numbers = parse_line(line)
        hits = get_hit_count(winning_numbers, my_numbers)
        copies = [idx + i + 1 for i in range(hits)]
        for i in copies:
            inventory[i] += inventory[idx]
    print(sum(inventory.values()))

if __name__ == "__main__":
    main()