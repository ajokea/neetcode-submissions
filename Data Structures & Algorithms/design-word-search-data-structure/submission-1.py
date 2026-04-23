class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.isWord = True    

    def search(self, word: str) -> bool:
        def helper(node, i):
            curr = node
            
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in curr.children.values():
                        if helper(child, j + 1):
                            return True
                    return False
                
                if word[j] not in curr.children:
                    return False
                
                curr = curr.children[word[j]]
            return curr.isWord
        
        return helper(self.root, 0)