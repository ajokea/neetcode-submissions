class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        n = max(counts.values())
        freq = [[] for _ in range(n)]
        for num in counts:
            freq[counts[num] - 1].append(num)

        result = []
        for i in range(n - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result