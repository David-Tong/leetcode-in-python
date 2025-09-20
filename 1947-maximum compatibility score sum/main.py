class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(students)
        N = len(students[0])
        scores = [[0] * M for _ in range(M)]
        for x in range(M):
            for y in range(M):
                for z in range(N):
                    scores[x][y] += students[x][z] == mentors[y][z]
        # print(scores)

        # process
        # dp init
        # dp[state] - max compatibility scores when the combination of mentors of state are selected
        #           - the number of mentors is the number of 1 in the state, for m
        #           - and same number of student for 0 to m - 1 are selected
        L = 2 ** M
        dp = [0] * L

        # dp transfer
        # for mentor in mentors of the combination of state
        # the student to be selected in this turn
        # dp[state] - max(dp[state], dp[state - mentor] + scores[student][mentor]
        for state in range(L):
            student = str(bin(state)).count("1") - 1
            for mentor in range(M):
                if state>>mentor & 1:
                    dp[state] = max(dp[state], dp[state ^ 1<<mentor] + scores[student][mentor])
        # print(dp)
        ans = dp[L - 1]
        return ans


students = [[1,1,0],[1,0,1],[0,0,1]]
mentors = [[1,0,0],[0,0,1],[1,1,0]]

"""
students = [[0,0],[0,0],[0,0]]
mentors = [[1,1],[1,1],[1,1]]
"""

solution = Solution()
print(solution.maxCompatibilitySum(students, mentors))
