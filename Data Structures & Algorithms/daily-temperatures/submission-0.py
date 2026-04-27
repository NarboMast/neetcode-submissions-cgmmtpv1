class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                past_t, past_day_ind = stack.pop()

                res[past_day_ind] = i - past_day_ind

            stack.append((t,i))

        return res
