class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort()

        stack = []
        for car in cars[::-1]:
            time = (target - car[0]) / car[1]
            if not stack or (stack and stack[-1] < time):
                stack.append(time)
            print(stack, time)
        
        return len(stack)
