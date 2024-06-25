class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter([ele for ele in nums if ele % 2 == 0])

        count = -1
        maxCount = -1

        for key, value in freq.items():
            if value > count or (value == count and key < maxCount):
                count = value
                maxCount = key
        
        return maxCount
