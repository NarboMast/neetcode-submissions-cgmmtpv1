class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = (
            (0, -1), #left
            (-1, 0), #up
            (0, 1), #right
            (1, 0) #down
            )

        def exploreIsland(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or
                c >= len(grid[0]) or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                exploreIsland(r + dr, c + dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    exploreIsland(r, c)
                    islands += 1

        return islands
        