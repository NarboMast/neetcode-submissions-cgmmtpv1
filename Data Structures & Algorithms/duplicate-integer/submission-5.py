class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()

        for n in nums:
            if n in checked:
                return True
            checked.add(n)

        return False