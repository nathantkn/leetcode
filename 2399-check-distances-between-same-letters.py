class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        myDict = {}

        for i in range(len(s)):
            if s[i] in myDict:
                index = ord(s[i]) - 97
                if distance[index] != (i - myDict[s[i]] - 1):
                    return False
            
            myDict[s[i]] = i
        
        return True
