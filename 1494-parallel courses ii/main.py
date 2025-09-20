class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = 2 ** n

        # count course number of a state
        courses = [0] * L
        for state in range(L):
            courses[state] = bin(state).count('1')
        # print(courses)

        # calculate a prerequisite courses of a state
        pre_courses = [0] * n
        for relation in relations:
            pre_courses[relation[1] - 1] |= 1 << (relation[0] - 1)
        # print(pre_courses)

        # prerequisites - prerequisites[state] - the prerequisites taken course combination for the state
        prerequisites = [0] * L
        for state in range(L):
            for x in range(n):
                if state >> x & 1:
                    prerequisites[state] |= pre_courses[x]
        # print(prerequisites)

        # process
        # dp init
        # dp[state] - minimal number of semesters to take all course of combination state
        dp = [float("inf")] * L
        for state in range(L):
            if prerequisites[state] == 0:
                if courses[state] <= k:
                    dp[state] = 1
        dp[0] = 0

        # dp transfer
        # dp[state] = min(dp[state], dp[subset] + dp[state - subset])
        for state in range(L):
            # check if state is valid
            # pruning, otherwise TLE
            if state & prerequisites[state] != prerequisites[state]:
                continue
            # loop over all subsets
            previous = state
            while previous:
                # check conditions
                #  1 : previous state subset is a subset of state
                #  2 : the course in state - subset is less than or equal to k
                if courses[state] - courses[previous] <= k:
                    # 3 : the previous state includes all prerequisites of state
                    if previous & prerequisites[state] == prerequisites[state]:
                        dp[state] = min(dp[state], dp[previous] + 1)
                previous = (previous - 1) & state
        # print(dp)
        ans = dp[L - 1]
        return ans


"""
n = 4
relations = [[2,1],[3,1],[1,4]]
k = 2

n = 5
relations = [[2,1],[3,1],[4,1],[1,5]]
k = 2

n = 6
relations = [[1,6],[2,6],[3,5],[4,5]]
k = 3

n = 14
relations = [[11,7]]
k = 2

n = 15
relations = [[12,11]]
k = 12
"""

n = 15
relations = []
k = 4

solution = Solution()
print(solution.minNumberOfSemesters(n, relations, k))
