class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {0: -1}
        remainder = 0

        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k

            if remainder not in remainderMap:
                remainderMap[remainder] = i
            elif i - remainderMap[remainder] > 1:
                return True      
        
        return False
