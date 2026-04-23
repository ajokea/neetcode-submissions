class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            charCount = [0 for i in range(26)]
            for char in s:
                charCount[ord(char) - ord('a')] += 1
            charCountTuple = tuple(charCount)
            groups[charCountTuple] = groups.get(charCountTuple, []) + [s]
        
        return groups.values()
