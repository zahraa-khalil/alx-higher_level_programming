#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    int_sum = 0
    for char in roman_string:
        int_sum += roman_dict[char]
    return int_sum
