class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for elem in nums:
            if elem + diff in nums and elem + 2 * diff in nums:
                res += 1
        return res
