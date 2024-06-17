class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            elif operation == "+":
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(operation))
        
        return sum(stack)
