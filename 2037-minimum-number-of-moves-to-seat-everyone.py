class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        maxNum = max(max(seats), max(students)) + 1
        seatsFreq = [0] * maxNum
        studentsFreq = [0] * maxNum

        for seat in seats:
            seatsFreq[seat] += 1

        for student in students:
            studentsFreq[student] += 1

        seatsPointer, studentsPointer = 0, 0
        res = 0
        remain = len(students)

        while remain:
            while seatsFreq[seatsPointer] == 0:
                seatsPointer += 1
            
            while studentsFreq[studentsPointer] == 0:
                studentsPointer += 1

            res += abs(seatsPointer - studentsPointer)
            seatsFreq[seatsPointer] -= 1
            studentsFreq[studentsPointer] -= 1
            remain -= 1
        
        return res
