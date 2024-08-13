class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isEnoughCapacity(capacity: int) -> bool:
            totalWeight, daysCount = 0, 1

            for weight in weights:
                if totalWeight + weight > capacity:
                    daysCount += 1
                    totalWeight = 0
                    if daysCount > days:
                        return False
                totalWeight += weight
            
            return True 
        
        low, high = max(weights), sum(weights)

        while low < high:
            mid = low + (high - low) // 2
            if isEnoughCapacity(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
