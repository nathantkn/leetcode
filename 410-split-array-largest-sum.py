class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isSmallestPossibleSum(capacity: int) -> bool:
            total, arrCount = 0, 1

            for num in nums:
                if total + num > capacity:
                    arrCount += 1
                    total = 0
                    if arrCount > k:
                        return False
                total += num
            return True 
        
        low, high = max(nums), sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            if isSmallestPossibleSum(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
