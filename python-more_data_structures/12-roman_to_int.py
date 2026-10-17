#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
            return 0
    
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    n = len(roman_string)
    
    for i in range(n):
        if i + 1 < n and roman_num[roman_string[i]] < roman_num[roman_string[i + 1]]:
            total -= roman_num[roman_string[i]]
        else:
            total += roman_num[roman_string[i]]
    return total
