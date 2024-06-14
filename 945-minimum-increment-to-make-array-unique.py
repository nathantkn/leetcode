class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = [0] * (len(nums) + max(nums) + 1)

        for val in nums:
            freq[val] += 1
        
        res = 0

        for i in range(len(freq)):
            if freq[i] > 1:
                dups = freq[i] - 1
                freq[i + 1] += dups
                freq[i] = 1
                res += dups
        
        return res
