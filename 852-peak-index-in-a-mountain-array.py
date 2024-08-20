class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2           
            if arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low
