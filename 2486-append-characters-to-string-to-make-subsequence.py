class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tPointer = 0
        tLen = len(t)

        for ch in s:
            if ch == t[tPointer]:
                tPointer += 1
                if tPointer == tLen:
                    return 0
        
        return tLen - tPointer
