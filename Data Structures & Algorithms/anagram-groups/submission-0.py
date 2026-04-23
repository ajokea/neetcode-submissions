class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            groups[sortedS] = groups.get(sortedS, []) + [s]
        
        return groups.values()