class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_ = 0
        
        stack = [] # i : h
        for i, h in enumerate(heights):
            i_ = i
            while stack and h < stack[-1][1]:
                i_, h_ = stack.pop()

                max_ = max(max_, ((i - i_) * h_))

            stack.append((i_, h))

        while stack:
            i, h = stack.pop()

            max_ = max(max_, ((len(heights) - i) * h))


        return max_
        