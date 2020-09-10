#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    valid_chr = ["I", "V", "X", "L", "C", "D", "M"]
    for c in roman_string:
        if c not in valid_chr:
            return 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    s = roman_string
    if s.find("IX") != -1:
        s = s.replace("IX", "VIIII")
    if s.find("XL") != -1:
        s = s.replace("XL", "XXXX")
    if s.find("XC") != -1:
        s = s.replace("XC", "LXXXX")
    if s.find("CD") != -1:
        s = s.replace("CD", "CCCC")
    if s.find("CM") != -1:
        s = s.replace("CM", "DCCCC")
    ls = list(s)
    for ch in ls:
        sum += d.get(ch)
    return sum
