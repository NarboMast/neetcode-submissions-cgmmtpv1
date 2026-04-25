class Solution:
    '''
    [5 ,1 ,2 ,10,6 ,2 ,7 ,9 ,3,1]
    [27,23,18,22,16,12,10,10,3,1]
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        robbed = [0] * len(nums)
        robbed[-2], robbed[-1] = nums[-2], nums[-1]
        
        max_ = robbed[-1]
        max_candidate = robbed[-2]

        for i in range(len(nums) - 3, -1, -1):
            robbed[i] = nums[i] + max_

            max_ = max(max_, max_candidate)
            max_candidate = robbed[i]

        return max(robbed[0], robbed[1])
        