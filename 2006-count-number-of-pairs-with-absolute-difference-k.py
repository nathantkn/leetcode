class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        myDict = defaultdict(int)
        res = 0

        for num in nums:
            myDict[num] += 1

        for num in nums:
            res += myDict[k + num]
        
        return res
