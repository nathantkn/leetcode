class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = [0, 0]
        for student in students:
            freq[student] += 1

        for sandwich in sandwiches:
            if freq[sandwich] > 0:
                freq[sandwich] -= 1
            else:
                return freq[0] + freq[1]
        
        return 0
