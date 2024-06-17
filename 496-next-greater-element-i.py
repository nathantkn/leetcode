class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        res = []
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            res.append(mapping.get(num, -1))

        return res
