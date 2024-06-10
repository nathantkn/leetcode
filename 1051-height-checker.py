class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copyList = sorted(heights)
        count = 0

        for i in range(len(copyList)):
            if copyList[i] != heights[i]:
                count += 1      

        return count
