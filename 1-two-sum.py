class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        n = len(nums)
        
        for i in range(n):
            complement = target - nums[i]
            if complement in myMap:
                return [myMap[complement], i]
            myMap[nums[i]] = i
            
        return []
