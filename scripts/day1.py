from utils import InputReader
import re

def _find_all_digits(line: str):
    search_pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d{1}))'
    return list(re.finditer(search_pattern, line))

def get_digits(line: str):
    m = _find_all_digits(line)
    first_digit = _convert_strings_to_digits(min(m, key=lambda x: x.span()[0]).group(1))
    last_digit = _convert_strings_to_digits(max(m, key=lambda x: x.span()[1]).group(1))
    return first_digit, last_digit
        
def _convert_strings_to_digits(string: str):
    '''
    Replaces all strings of digits as int-like.
    If string is not in digit_map keys (already int-like), return self'''
    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return digit_map.get(string, string)

def get_calibration_values(data):
    '''Takes a line as input and returns the calibration value.
    The calibration value is defined as the concatenation of first and last digit in each string.'''
    for line in data:
        digits = get_digits(line)
        yield int(''.join(digits))

def main():
    reader = InputReader(1)
    data = reader.split_lines()
    print(sum(get_calibration_values(data)))

if __name__ == "__main__":
    main()