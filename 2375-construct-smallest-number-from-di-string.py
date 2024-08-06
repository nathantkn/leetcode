class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [1]
        tmp = []
        curr = 2

        for c in pattern:
            if c == 'I':
                while tmp:
                    stack.append(tmp.pop())
            else:
                tmp.append(stack.pop())
            
            stack.append(curr)
            curr += 1
        
        while tmp:
            stack.append(tmp.pop())
        
        res = ""
        for num in stack:
            res += str(num)
        
        return res
