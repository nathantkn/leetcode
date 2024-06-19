class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        minDiff = math.inf

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[1]:
                continue
            
            left, right = i + 1, n - 1

            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == target:
                    return sum
                elif sum > target:
                    right -= 1
                else:
                    left += 1
                
                diff = abs(sum - target)
                if diff < minDiff:
                    minDiff = diff
                    closest = sum
        
        return closest
