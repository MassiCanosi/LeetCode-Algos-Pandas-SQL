class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_rev = str(x)[::-1]
        if str(x) == x_rev:
            return True
        else:
            return False
        