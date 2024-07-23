class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # pre-process
        L = len(seats)
        seats = sorted(seats)
        students = sorted(students)

        # process
        ans = 0
        for x in range(L):
            ans += abs(students[x] - seats[x])
        return ans


seats = [3,1,5]
students = [2,7,4]

seats = [4,1,5,9]
students = [1,3,2,6]

seats = [2,2,6,6]
students = [1,3,2,6]

solution = Solution()
print(solution.minMovesToSeat(seats, students))
