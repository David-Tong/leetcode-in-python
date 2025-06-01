from collections import defaultdict


class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        # pre-process
        M = len(seats)
        N = len(seats[0])

        # helper function
        # generate valid state
        states = [defaultdict(int) for _ in range(N)]
        def generateValidState(row, col, state, student):
            if row == M:
                states[col][state] = student
            else:
                if seats[row][col] == ".":
                    generateValidState(row + 1, col, state + "1", student + 1)
                generateValidState(row + 1, col, state + "0", student)

        # generate all valid states for every column
        for col in range(N):
            generateValidState(0, col, "", 0)
        # print(states)

        # check if it can transfer from one state to other state
        def canTransfer(state, other):
            for row in range(M):
                if other[row] == "1":
                    if state[row] == "1":
                        return False
                    if row> 0:
                        if state[row - 1] == "1":
                            return False
                    if row < M - 1:
                        if state[row + 1] == "1":
                            return False
            return True

        # process
        # dp transfer
        # dp[col][state] - the number of students taking exam with col columns and state state.
        dp = [defaultdict(int) for _ in range(N)]
        for col in range(N):
            if col == 0:
                dp[col] = states[col]
            else:
                for s in states[col - 1]:
                    for ns in states[col]:
                        if canTransfer(s, ns):
                            dp[col][ns] = max(dp[col][ns], dp[col -1][s] + states[col][ns])
        # print(dp)

        # post-process
        ans = 0
        for s in dp[N - 1]:
            ans = max(ans, dp[N - 1][s])
        return ans


seats = [["#",".","#","#",".","#"],
         [".","#","#","#","#","."],
         ["#",".","#","#",".","#"]]

seats = [[".","#"],
         ["#","#"],
         ["#","."],
         ["#","#"],
         [".","#"]]

seats = [["#",".",".",".","#"],
         [".","#",".","#","."],
         [".",".","#",".","."],
         [".","#",".","#","."],
         ["#",".",".",".","#"]]

seats = [[".","#","#","."],
         [".",".",".","#"],
         [".",".",".","."],
         ["#",".","#","#"]]

solution = Solution()
print(solution.maxStudents(seats))
