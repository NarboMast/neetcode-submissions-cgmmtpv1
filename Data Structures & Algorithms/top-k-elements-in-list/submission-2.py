class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = [[] for _ in range(len(nums) + 1)]

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, freq in count.items():
            bucket_sort[freq].append(n)

        print(bucket_sort)

        res = []

        for i in bucket_sort[::-1]:
            for j in i:
                if len(res) < k:
                    res.append(j)
                else:
                    break
        
        return res
