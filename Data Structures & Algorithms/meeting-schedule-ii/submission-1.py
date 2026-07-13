"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i : i.start)
        count = 0

        used_rooms = [] #end
        empty_rooms = 0

        for interval in intervals:
            s, e = interval.start, interval.end

            while used_rooms and s >= used_rooms[0]:
                heapq.heappop(used_rooms)
                empty_rooms += 1

            if empty_rooms > 0:
                empty_rooms -= 1
            else:
                count += 1

            heapq.heappush(used_rooms, e)

        return count
        