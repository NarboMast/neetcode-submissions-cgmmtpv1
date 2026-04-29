class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)

        print(graph)

        def dfs(key, visited):
            if key in visited:
                return False

            if key not in graph:
                return True

            visited.add(key)
            neighbors = graph[key]

            for nei in neighbors:
                if not dfs(nei, visited):
                    return False
            
            graph[key] = []
            visited.remove(key)
            return True

        for key in graph:
            if not dfs(key, set()):
                return False
            
        return True
        