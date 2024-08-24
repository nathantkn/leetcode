class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(find: int) -> int:
            idx, low, high = -1, 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx
        
        def findLast(find: int) -> int:
            idx, low, high = -1, 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx
        
        res = [-1, -1]
        res[0] = findFirst(target)
        res[1] = findLast(target)

        return res
