class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIdx, popIdx = 0, 0

        for push in pushed:
            pushed[pushIdx] = push
            while pushIdx >= 0 and pushed[pushIdx] == popped[popIdx]:
                pushIdx -= 1
                popIdx += 1
                
            pushIdx += 1
                
        return pushIdx == 0
