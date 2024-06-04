class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        count = 0
        middleLetter = False

        for value in freq.values():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                middleLetter = True
            
        if middleLetter:
            return count + 1
        return count

    def longestPalindrome2(self, s: str) -> int:
        seen = set()
        count = 0

        for i in s:
            if i in seen:
                count += 2
                seen.remove(i)
            else:
                seen.add(i)
        
        if seen:
            count += 1
        
        return count
