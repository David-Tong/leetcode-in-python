class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        m = 3

        # helper function
        # generate all valid states for 3 grid a row
        states = list()
        def generateValidStates(state):
            if len(state) == m:
                states.append(state)
            else:
                for x in range(m):
                    if state == "" or state[-1] != str(x):
                        generateValidStates(state + str(x))

        # check if state of previous row can transfer to the other state of the current row
        def canTransfer(state, other):
            for x in range(m):
                if state[x] == other[x]:
                    return False
            return True

        # process
        # generate all valid states
        generateValidStates("")
        S = len(states)

        # dp transfer
        # dp[x][state] - the number of ways to paint n x 3 grid in the xth row with state
        # state - eg. 101 yellow, red, yello
        #             0 for red, 1 for yellow, 2 for green
        # using rolling array
        from collections import defaultdict
        prev = defaultdict(int)
        for s in states:
            prev[s] = 1
            
        for x in range(1, n):
            curr = defaultdict(int)
            for s in states:
                for ns in states:
                    if canTransfer(s, ns):
                        curr[ns] = (curr[ns] + prev[s]) % MODULO
            prev = curr

        # post-process
        print(prev)
        ans = 0
        for s in prev:
            ans = (ans + prev[s]) % MODULO
        return ans


n = 1
n = 5000
n = 2
n = 4

solution = Solution()
print(solution.numOfWays(n))
