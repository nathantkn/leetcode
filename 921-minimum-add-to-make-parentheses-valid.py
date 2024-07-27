class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openB, closeB = 0, 0

        for c in s:
            if openB > 0 and c == ')':
                openB -= 1
            elif c == '(':
                openB += 1
            else:
                closeB += 1
        
        return openB + closeB
