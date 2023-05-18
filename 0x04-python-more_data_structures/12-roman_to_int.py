#!/usr/bin/python3

# converts Roman numerals into integer

def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, int):
        return 0

    roman_numeral = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in roman_numeral:
            return 0

    for i, c in enumerate(roman_string):
        if ((i + 1) == len(roman_string) or roman_numeral[c]
                >= roman_numeral[roman_string[i + 1]]):
            total += roman_numeral[c]
        else:
            total -= roman_numeral[c]

    return total
