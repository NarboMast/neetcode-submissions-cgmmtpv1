class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res = []

        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
