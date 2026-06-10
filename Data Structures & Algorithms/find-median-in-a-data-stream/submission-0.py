class MedianFinder:

    def __init__(self):
        self.smaller = [] #max heap
        self.bigger = [] #min heap

    def addNum(self, num: int) -> None:
        if self.bigger and self.bigger[0] <= num:
            heapq.heappush(self.bigger, num)
        else:
            heapq.heappush(self.smaller, -num)

        if len(self.smaller) - 1 > len(self.bigger):
            transfer = -heapq.heappop(self.smaller)
            heapq.heappush(self.bigger, transfer)
        elif len(self.bigger) - 1 > len(self.smaller):
            transfer = heapq.heappop(self.bigger)
            heapq.heappush(self.smaller, -transfer)

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (-self.smaller[0] + self.bigger[0]) / 2
        
        if len(self.smaller) > len(self.bigger):
            return -self.smaller[0]
        else:
            return self.bigger[0]
        