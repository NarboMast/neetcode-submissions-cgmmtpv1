class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = (
            (0, -1), #left
            (-1, 0), #up
            (0, 1), #right
            (1, 0) #down
        )

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def calcDistance(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == -1 or
                (r, c) in visited
            ): return

            visited.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for rd, cd in directions:
                    calcDistance(r + rd, c + cd)

            dist += 1

        
        