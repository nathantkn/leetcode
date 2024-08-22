class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[max(0, mid - 1)] > nums[mid]:
                high = mid
            elif nums[mid + 1] > nums[mid]:
                low = mid + 1
            else:
                return mid
        
        return low
