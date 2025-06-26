class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_adj = s.strip().split()[-1]
        return len(s_adj)