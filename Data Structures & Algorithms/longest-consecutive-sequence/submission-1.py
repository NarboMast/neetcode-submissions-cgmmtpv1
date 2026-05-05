class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = set(nums)
        streak = 0

        for n in nums:
            if n - 1 not in nums_:
                temp_streak = 1
                while n + 1 in nums_:
                    temp_streak += 1
                    n += 1
                streak = max(streak, temp_streak)

        return streak
        