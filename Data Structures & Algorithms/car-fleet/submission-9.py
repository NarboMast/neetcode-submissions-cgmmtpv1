import bisect

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = []

        for i in range(len(position)):
            bisect.insort(highway, [position[i], speed[i]])

        fleet = []
        
        for i in range(len(highway) - 1, -1, -1):
            time = float(target - highway[i][0]) / highway[i][1]

            if fleet and time <= fleet[-1]:
                continue
        
            fleet.append(time)

        return len(fleet)
        