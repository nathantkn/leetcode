class Solution:
    def reverseParentheses(self, s: str) -> str:
        index, res = [], []

        for c in s:
            if c == '(':
                index.append(len(res))
            elif c == ')':
                openParentIndex = index.pop()
                res[openParentIndex:] = res[openParentIndex:][::-1]
            else:
                res.append(c)
        
        return "".join(res)
