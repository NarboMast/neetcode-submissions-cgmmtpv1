class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = (
            (0,-1),
            (0,1),
            (-1, 0),
            (1, 0)
        )

        candidates = []

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    candidates.append((r,c))

        def dfs(r, c, i):
            if i == len(word): return True

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                word[i] != board[r][c] or
                board[r][c] == '#'
            ): return False

            board[r][c] = '#'
            res = False

            for rd, cd in directions:
                nr, nc = r + rd, c + cd

                if not res:
                    res = dfs(nr,nc,i+1)
            
            board[r][c] = word[i]
            return res
        
        for r, c in candidates:
            if dfs(r,c,0):
                return True

        return False
