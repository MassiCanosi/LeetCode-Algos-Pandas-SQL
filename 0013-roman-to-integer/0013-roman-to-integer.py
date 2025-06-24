class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        roman_number = s
        total = 0
        _diff = 0

        for i, char in enumerate(roman_number):

            int_char = mapping[char]
            total += int_char
            total -= _diff
            _diff = 0

            try:

                if char == "C" and (roman_number[i+1] == "M" or roman_number[i+1] == "D"):
                    _diff = 100*2
                elif char == "X" and (roman_number[i+1] == "L" or roman_number[i+1] == "C"):
                    _diff = 10*2
                elif char == "I" and (roman_number[i+1] == "V" or roman_number[i+1] == "X"):
                    _diff = 1*2

            except IndexError:
                break

        return total

