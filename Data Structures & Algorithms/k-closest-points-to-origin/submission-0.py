class Solution:
    '''
    the problem involves a min heap with calculation of euclidean distance.
    the main issue is to convert the formula back to indexies. 
    potentially, the methods which compare vals in heap may be overriden like a hash function in hashmap
    '''
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x*x + y*y

            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [(x, y) for _, x, y in heap]
        