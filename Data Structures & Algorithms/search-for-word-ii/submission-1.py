class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        rows, cols = len(board), len(board[0])

        def dfs(row, col, word, i):
            if i == len(word):
                return True

            if (
                row not in range(rows) or
                col not in range(cols) or
                (row, col) in visited or
                board[row][col] != word[i]):
                return False
            
            visited.add((row, col))
            
            paths = (
                dfs(row - 1, col, word, i + 1) or 
                dfs(row + 1, col, word, i + 1) or 
                dfs(row, col - 1, word, i + 1) or 
                dfs(row, col + 1, word, i + 1)
            )
            
            visited.remove((row, col))

            return paths
            

        for word in words:
            visited = set()
            flag = False
            for r in range(rows):
                for c in range(cols):
                    if dfs(r, c, word, 0):
                        result.append(word)
                        flag = True
                        break
                if flag:
                    break

        return result