class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_ = 0
        RAWS = len(grid)
        COLS = len(grid[0])
        directions = (
            (0, -1), #left
            (-1, 0), #up
            (0, 1), #right
            (1, 0)  #down
        )

        def exploreIsland(r, c):
            nonlocal max_
            size = 1
            grid[r][c] = 0
            q = collections.deque()
            q.append((r, c))

            while q:
                rc, cc = q.popleft()
                for rd, cd in directions:
                    nr, nc = rc + rd, cc + cd
                    if (
                        nr >= RAWS or
                        nc >= COLS or
                        nr < 0 or
                        nc < 0
                    ): continue

                    if grid[nr][nc] == 1:
                        size += 1
                        q.append((nr, nc))
                        grid[nr][nc] = 0

            max_ = max(max_, size)

        for r in range(RAWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    exploreIsland(r, c)

        return max_
        