class Solution:
    '''
    [1,2,1,2,1,1,1] 0
    [4,5,3,3,2,1,1]

    [1,2,3]
    [3,2,3]
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prices = [0] * len(cost)
        prices[-2], prices[-1] = cost[-2], cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            prices[i] = min(prices[i+1], prices[i+2]) + cost[i]

        return min(prices[0], prices[1])
        