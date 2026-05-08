class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = (
            (0, -1), #left
            (0, 1), #right
            (-1, 0), #up
            (1, 0) 
        )

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == '0'
            ): return

            grid[r][c] = '0'

            for rd, cd in directions:
                dfs(rd + r, c + cd)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
        