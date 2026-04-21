class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l_max, r_max = height[0], height[len(height)-1]
        l, r = 0, len(height) - 1
        while l < r:
            min_ = min(height[l], height[r])
            temp = 0

            if min_ == height[l]:
                temp = l_max - height[l]

                l_max = max(height[l], l_max)
                l += 1
            else:
                temp = r_max - height[r]

                r_max = max(height[r], r_max) 
                r -= 1

            res += temp if temp > 0 else 0

        return res