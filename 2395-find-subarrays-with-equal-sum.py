class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        myDict = defaultdict(int)

        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1]) in myDict:
                return True
            
            myDict[nums[i] + nums[i + 1]] += 1
        
        return False
