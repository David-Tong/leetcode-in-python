class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # pre-process
        L = m ** 3
        MODULO = 10 ** 9 + 7

        # helper function
        # generate valid states
        states = list()
        def generateValidStates(state):
            if len(state) == m:
                states.append(state)
            else:
                for x in range(3):
                    if state == "" or state[-1] != str(x):
                        generateValidStates(state + str(x))

        # helper function
        # check if one state can transfer from the previous row to the another state
        def checkValid(state, state2):
            for x in range(m):
                if state[x] == state2[x]:
                    return False
            return True

        # process
        # generate valid states
        generateValidStates("")

        # dp[x][state] - the number of ways to color the grid in xth column with color combination of state
        # state - eg. 01212 0 for red, 1 for green, and 2 for blue
        #             row 0 for red, row 1 for green, row 2 for blue, row 3 for green, row 4 for blue
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(n)]

        for x in range(n):
            if x == 0:
                for s in states:
                    dp[x][s] = 1
            else:
                for s in states:
                    for ns in states:
                        if checkValid(s, ns):
                            dp[x][ns] = (dp[x][ns] + dp[x - 1][s]) % MODULO

        # post-process
        ans = 0
        for s in dp[n - 1]:
            ans = (ans + dp[n - 1][s]) % MODULO
        return ans


m = 5
n = 5

solution = Solution()
print(solution.colorTheGrid(m, n))
