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
        prev = 0

        for char roman_number:

            current_value = mapping[char]

            if prev < current_value:
                total += (current_value - prev * 2)
            else:
                total += current_value

            prev = current_value

        return total

