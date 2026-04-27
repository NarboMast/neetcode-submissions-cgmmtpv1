import bisect

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = sorted([(p,s) for p,s in zip(position,speed)])

        fleet = []
        
        for i in range(len(highway) - 1, -1, -1):
            time = float(target - highway[i][0]) / highway[i][1]

            if fleet and time <= fleet[-1]:
                continue
        
            fleet.append(time)

        return len(fleet)
        