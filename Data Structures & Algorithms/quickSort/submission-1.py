# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
    
        def recursion(start, end):
            if end - start + 1 <= 1:
                return
            
            pivot = pairs[end]
            left = start
            for i in range(start, end):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1

            pairs[left], pairs[end] = pairs[end], pairs[left]
            recursion(start, left - 1)
            recursion(left + 1, end)

        recursion(0, len(pairs) - 1)
        return pairs
