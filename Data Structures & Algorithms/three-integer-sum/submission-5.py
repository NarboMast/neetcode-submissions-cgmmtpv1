class Solution:
    # -4, -1, -1, 0, 1, 2
    # -1, 2, -1
    # -1, 1, 0

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        checked = set()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = nums[i]

            while l < r:
                diff = target +  nums[l] + nums[r]
                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        