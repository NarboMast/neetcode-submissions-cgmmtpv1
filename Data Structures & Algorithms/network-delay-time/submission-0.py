class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))

        min_heap = [(0, k)]
        res = 0
        visited = set()
        
        while min_heap:
            curr_w, curr_n = heapq.heappop(min_heap)
            
            if curr_n in visited: continue

            visited.add(curr_n)
            res = max(res, curr_w)

            for v, w in edges[curr_n]:
                if v not in visited: 
                    heapq.heappush(min_heap,(w+curr_w, v))

        return res if len(visited) == n else -1
