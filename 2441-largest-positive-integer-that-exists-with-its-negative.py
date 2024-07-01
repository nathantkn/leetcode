class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxNum = -1

        for num in nums:
            if -num in mySet:
                maxNum = max(num, maxNum)

        return maxNum
