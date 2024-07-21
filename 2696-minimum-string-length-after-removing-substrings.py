class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if stack and (stack[-1] + c == "AB" or stack[-1] + c == "CD"):
                stack.pop()
            else:
                stack.append(c)
        
        return len("".join(stack))
