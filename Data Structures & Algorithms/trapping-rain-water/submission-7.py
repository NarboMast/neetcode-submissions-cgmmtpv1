class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        while l <= r:
            min_ = min(height[l], height[r])
            trapped = 0

            if min_ == height[l]:
                trapped = l_max - height[l]
                l_max = max(height[l], l_max)
                l+=1
            else:
                trapped = r_max - height[r]
                r_max = max(height[r], r_max)
                r-=1
            
            res += trapped if trapped > 0 else 0

        return res