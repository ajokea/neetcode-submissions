class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node

            for j in range(i, len(word)):
                if word[j] == '.':
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                
                if word[j] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[j]]
            return curr.endOfWord
        
        return dfs(0, self.root)