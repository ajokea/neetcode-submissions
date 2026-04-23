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

        result = []
        
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, word):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] not in node.children or
                (r, c) in visited):
                return
            
            visited.add((r, c))
            word.append(board[r][c])
            node = node.children[board[r][c]]
            if node.isWord:
                result.append("".join(word))
                node.isWord = False
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            word.pop()
            visited.remove((r, c))


        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, [])

        return result