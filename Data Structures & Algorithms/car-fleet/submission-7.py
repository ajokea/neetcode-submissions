class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort()

        bottleneck = None
        fleets = n
        for car in cars[::-1]:
            time = (target - car[0]) / car[1]
            if bottleneck and time <= bottleneck:
                fleets -= 1
            else:
                bottleneck = time
        
        return fleets
