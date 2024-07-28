class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        strList = list(s)

        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    strList[i] = ''
            elif s[i] == '(':
                stack.append(i)
        
        for index in stack:
            strList[index] = ''
        
        return "".join(strList)
