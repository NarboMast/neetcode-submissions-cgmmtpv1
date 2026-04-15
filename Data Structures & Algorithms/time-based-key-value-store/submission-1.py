class TimeMap:
    # {key, {(key:1, happy), (key:3, sad)}}

    def __init__(self):
        self.kvts : Map(str, []) = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvts:
            self.kvts[key] = []
        self.kvts[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        vts = self.kvts.get(key, [])

        l, r = 0, len(vts) - 1
        while l <= r:
            m = (l + r) // 2

            if vts[m][0] <= timestamp:
                res = vts[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

