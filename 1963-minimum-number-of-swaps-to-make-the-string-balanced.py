class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        
        for c in s:
            if unbalanced > 0 and c == ']':
                unbalanced -= 1
            else:
                unbalanced += 1
        
        return (unbalanced + 1) // 2
