class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        myDict = defaultdict(int)

        while len(nums) != 0:
            average = (nums[0] + nums[-1]) / 2
            nums.pop(0)
            nums.pop(-1)
            myDict[average] += 1
        
        return len(myDict)
