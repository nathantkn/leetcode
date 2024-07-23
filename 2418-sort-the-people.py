class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        freqMap = {}
        n = len(heights)

        for i in range(n):
            freqMap[heights[i]] = names[i]
        
        heights.sort()
        count = 0

        for i in reversed(range(n)):
            names[count] = freqMap[heights[i]]
            count += 1
        
        return names
