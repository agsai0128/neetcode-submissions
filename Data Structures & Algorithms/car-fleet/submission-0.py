class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0

        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))

        cars.sort(reverse = True, key = lambda x:x[0])

        fleets = 0
        slowest_time = 0.0
        for _, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets