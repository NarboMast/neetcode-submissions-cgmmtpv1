class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        graph = {i : [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(key, prev):
            if key in visited:
                return False

            visited.add(key)

            for nei in graph[key]:
                if nei == prev:
                    continue

                if not dfs(nei, key):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
