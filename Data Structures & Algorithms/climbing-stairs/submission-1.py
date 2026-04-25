class Solution:
    '''
    n = 3

    1 = 1
    2 = 2
    3 = 3
    4 = 5
    5 = 8
    6 = 13
    7 = 21
    8 = 34
    '''
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        steps = [0] * n
        steps[0], steps[1] = 1, 2

        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[-1]
        