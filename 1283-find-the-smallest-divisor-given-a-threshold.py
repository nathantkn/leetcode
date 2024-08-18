class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def findSum(divisor: int):
            currSum = 0
            for num in nums:
                currSum += ceil(num / divisor)

            return currSum
        
        low, high = 1, max(nums)

        while low < high:
            mid = low + (high - low) // 2
            if findSum(mid) <= threshold:
                high = mid
            else:
                low = mid + 1
        
        return low
