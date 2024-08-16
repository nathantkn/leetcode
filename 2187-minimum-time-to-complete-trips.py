class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def feasible(givenTime: int):
            tripsMade = 0

            for curr in time:
                tripsMade += givenTime // curr
                
            if tripsMade >= totalTrips:
                return True
            return False

        low, high = 1, min(time) * totalTrips

        while low < high:
            mid = low + (high - low) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1

        return low
