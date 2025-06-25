class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_start = 0
        window_end = len(needle)
        limit = len(haystack)
        otp = -1

        while window_end <= limit:
            sliding = haystack[window_start:window_end]

            if sliding == needle:
                otp = window_start
                break
            else:
                window_start += 1
                window_end += 1

        return otp