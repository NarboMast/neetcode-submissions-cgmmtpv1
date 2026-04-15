class Solution:
    #O(nlog(n)) -> compare
    #set of freq of chars -> compare sets O(n)
    #
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count : Map(str, int) = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)

        for c in t:
            if c in count and count[c] > 0:
                count[c] -= 1
            else:
                return False

        print(count)

        return True