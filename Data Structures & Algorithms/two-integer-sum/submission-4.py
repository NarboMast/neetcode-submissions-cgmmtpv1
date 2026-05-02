class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in checked:
                return [checked[diff], i]
            else:
                checked[n] = i

        return []
        