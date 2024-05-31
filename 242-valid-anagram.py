class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap = defaultdict(int)

        for x in s:
            myMap[x] += 1

        for i in t:
            myMap[i] -= 1

        for val in myMap.values():
            if val != 0:
                return False

        return True
