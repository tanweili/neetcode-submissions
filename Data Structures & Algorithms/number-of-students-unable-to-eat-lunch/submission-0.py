class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s0, s1 = 0, 0
        # Student order doesn't matter since they can rotate
        for i in range(len(students)): 
            if students[i] == 0:
                s0 += 1
            else:
                s1 += 1
        output = 0
        for i in range(len(sandwiches)):
            if sandwiches[i] == 0 and s0 > 0:
                s0 -= 1
            elif sandwiches[i] == 1 and s1 > 0:
                s1 -= 1
            else:
                output = len(sandwiches) - i
                break
        return output
