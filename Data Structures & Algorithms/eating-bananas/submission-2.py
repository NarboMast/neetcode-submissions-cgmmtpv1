class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # o(n) to find max
        max_ = piles[0]
        for n in piles:
            if max_ < n: max_ = n

        # log(max) to seach in the range
        ## o(n) to iterate piles with potential k
        k = max_
        l, r = 1, max_

        while l <= r:
            k_ = (l + r) // 2
            h_ = h

            for n in piles:
                if h_ < 0: break
                h_ -= math.ceil(n / k_)

            if h_ >= 0:
                k = k_
                r = k_ - 1
            else:
                l = k_ + 1
        
        return k