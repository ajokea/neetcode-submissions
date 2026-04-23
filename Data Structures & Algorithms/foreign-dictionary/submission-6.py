class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {char: set() for word in words for char in word}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            minLength = min(len(word1), len(word2))
            if (len(word1) > len(word2) and 
                word1[:minLength] == word2[:minLength]):
                return ""
            
            for j in range(minLength):
                if word1[j] != word2[j]:
                    adjacency[word1[j]].add(word2[j])
                    break

        result = []
        visited = {}
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for adj in adjacency[char]:
                if dfs(adj):
                    return True
            
            visited[char] = False
            result.append(char)
            return False
        
        for char in adjacency:
            if dfs(char):
                return ""

        return "".join(reversed(result))