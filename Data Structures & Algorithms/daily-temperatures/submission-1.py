class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                index = stack.pop()[1]
                result[index] = i - index
            stack.append([temp, i])

        return result