class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                
                if grid[r][c] == 1:
                    fresh += 1

        mins = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            mins += 1

        return mins if fresh == 0 else -1