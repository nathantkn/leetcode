class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maxNum = max(arr1)
        count = [0] * (maxNum + 1)

        for num in arr1:
            count[num] += 1
        
        res = []
        for num in arr2:
            while count[num] > 0:
                res.append(num)
                count[num] -= 1
            
        for i in range(maxNum + 1):
            while count[i] > 0:
                res.append(i)
                count[i] -= 1
        
        return res
