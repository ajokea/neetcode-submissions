class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort()

        bottleneck = None
        fleets = n
        for i in range(n - 1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if bottleneck and time <= bottleneck:
                fleets -= 1
            else:
                bottleneck = time
        
        return fleets
