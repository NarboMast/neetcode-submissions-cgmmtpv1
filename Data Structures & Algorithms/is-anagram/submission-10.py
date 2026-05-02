class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        a = ord('a')
        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - a] += 1
            freq[ord(t[i]) - a] -= 1

        for f in freq:
            if f != 0:
                return False

        return True
        