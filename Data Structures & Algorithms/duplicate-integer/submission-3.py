class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()

        for num in nums:
            if num in checked:
                return True
            else:
                checked.add(num)

        return False