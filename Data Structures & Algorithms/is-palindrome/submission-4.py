class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True
        l, r = 0, len(s) - 1
        res = False

        while l < r:
            while not self.isAlphaNumeric(s[l]) and l < r:
                l += 1

            while not self.isAlphaNumeric(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower(): return False
            res = True

            l += 1
            r -= 1

        return res

    def isAlphaNumeric(self, c):
        return (
            ('a' <= c <= 'z') or 
            ('A' <= c <= 'Z') or
            ('0' <= c <= '9')
               )
        