class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieTree()
        for word in words:
            root.insert(word)

        directions = (
            (0, -1), #left
            (-1, 0), #up
            (0, 1), #right
            (1, 0) #down
        )
        ROWS = len(board)
        COLS = len(board[0])

        res = set()

        def dfs(r, c, word, visited, node):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ): return

            char = board[r][c]

            visited.add((r, c))
            node = node.children[char]
            new_word = word + char

            if node.word_end:
                res.add(new_word)

            for rd, cd in directions:
                dfs(r + rd, c + cd, new_word, visited, node)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                dfs(r, c, '', visited, root.root)

        return list(res)
        