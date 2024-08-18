class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        def onTime(speed: float):
            totalTime = 0

            for i in range(len(dist) - 1):
                totalTime += ceil(dist[i] / speed)
            totalTime += dist[-1] / speed
            
            if totalTime > hour:
                return False
            return True
        
        low, high = 1, 10000000

        while low < high:
            mid = low + (high - low) // 2
            if onTime(mid):
                high = mid
            else:                
                low = mid + 1

        return low
