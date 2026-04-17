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
            jump = ''

            while s[i] != '@':
                jump += s[i]
                i += 1

            jump = int(jump)
            i += 1

            res.append(s[i:i+jump])
            i += jump

        return res
