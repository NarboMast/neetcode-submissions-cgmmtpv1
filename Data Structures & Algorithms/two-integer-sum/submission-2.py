class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}

        for i in range(len(nums)):
            curr = nums[i]

            if curr in reminder:
                return [reminder[curr], i]
            else:
                diff = target - curr
                reminder[diff] = reminder.get(diff, i)

        print(reminder)
        return []
        