class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = (
            (0, -1), #left
            (0, 1), #right
            (-1, 0), #up
            (1, 0) #down
        )

        def dfs(r, c):   
            if (
                r < 0 or r >= ROWS or
                c < 0 or c>= COLS or 
                board[r][c] != 'O'
            ): return

            board[r][c] = 'T'

            for rd, cd in directions:
                dfs(r + rd, c + cd)
                        
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
