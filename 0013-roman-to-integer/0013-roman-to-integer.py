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
        reversed_roman = roman_number[::-1]

        for i, char in enumerate(reversed_roman):

            current_value = mapping[char]

            if prev > current_value:
                print("sottraggo", current_value, "a", total)
                total -= current_value
            else:
                total += current_value

            prev = current_value

        return total

