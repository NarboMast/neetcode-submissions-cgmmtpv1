class Solution:
    '''
    to avoid looking for the heaviest two at each step, we can store them all in a max heap
    and pop two at each step until i have one left. After smashing, if remains, i insert into heap back
    Therefore popping takes us O(1) time and inserting takes O(log(n))
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        max_heap = []
        for n in stones:
            heapq.heappush(max_heap, -n)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            print(stone1, stone2)

            diff = stone1 - stone2

            if diff != 0:
                heapq.heappush(max_heap, -abs(diff))

        return -max_heap[0] if len(max_heap) == 1 else 0
        