class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible(days: int):
            flowerCount, bouquetCount = 0, 0

            for currDay in bloomDay:
                if currDay <= days:
                    flowerCount += 1
                    if flowerCount == k:
                        bouquetCount += 1
                        flowerCount = 0
                else:
                    flowerCount = 0
            
            if bouquetCount >= m:
                return True
            return False
        
        low, high = min(bloomDay), max(bloomDay)

        while low < high:
            mid = low + (high - low) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
                
        return low
