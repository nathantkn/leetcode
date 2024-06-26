class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        maxCurrIndex = 0
        n = len(nums)

        res = []

        for i in range(n):
            if nums[i] == key:
                start = max(maxCurrIndex, i - k)
                for j in range(start, min(n, i + k + 1)):
                    res.append(j)
                maxCurrIndex = min(n, i + k + 1)

        return res
