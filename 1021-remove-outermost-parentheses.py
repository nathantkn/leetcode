class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0

        for c in s:
            if c == ')':
                count -= 1
            if count > 0:
                res.append(c)
            if c == '(':
                count += 1
            
        return "".join(res)
