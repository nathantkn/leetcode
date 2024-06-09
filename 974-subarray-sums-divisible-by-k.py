class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderMap = {0: 1}
        remainder = 0
        res = 0

        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k

            if remainder in remainderMap:
                res += remainderMap[remainder]
                remainderMap[remainder] += 1
            else:
                remainderMap[remainder] = 1

        return res
