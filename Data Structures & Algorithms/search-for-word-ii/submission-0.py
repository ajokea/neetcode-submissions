class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        result = set()

        rows, cols = len(board), len(board[0])
        visited = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, node, word):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)
            
            for d in directions:
                dfs(r + d[0], c + d[1], node, word)
            
            visited.remove((r, c))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(result)