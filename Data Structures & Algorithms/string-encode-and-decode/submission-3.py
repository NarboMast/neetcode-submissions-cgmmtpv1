class Solution:
    # 5@Hello5@World

    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            res += str(len(word)) + '@' + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            start = i
            while s[i] != '@':
                i += 1

            jump = int(s[start:i])
            i += 1

            res.append(s[i:i+jump])
            i += jump

        return res
