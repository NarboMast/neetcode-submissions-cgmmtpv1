class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = (
            (0, -1), #left
            (-1, 0), #up
            (0, 1), #right
            (1, 0) #down
        )
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ): return

            visit.add((r, c))

            for rd, cd in directions:
                dfs(r + rd, c + cd, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res