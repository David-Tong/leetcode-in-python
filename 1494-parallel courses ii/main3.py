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

        # dependency
        from collections import defaultdict
        dicts = defaultdict(list)
        for relation in relations:
            prerequisite, successor = relation
            dicts[successor].append(prerequisite)
        # print(dicts)

        from collections import deque
        prerequisites = defaultdict(list)
        for successor in dicts:
            bfs = deque()
            prerequisite = dicts[successor]
            for pre in prerequisite:
                bfs.append(pre)
            while bfs:
                curr = bfs.popleft()
                prerequisites[successor].append(curr)
                if curr in dicts:
                    for nxt in dicts[curr]:
                        bfs.append(nxt)

        # get state
        def getState(courses):
            state = 0
            for course in courses:
                state += 1 << (course - 1)
            return state

        pre_states = defaultdict(int)
        for key in prerequisites:
            pre_states[key] = getState(prerequisites[key])
        # print(pre_states)

        # get courses
        cache = defaultdict(list)
        def getCourses(state):
            if state in cache:
                return cache[state]
            courses = list()
            idx = 1
            while state:
                if state & 1:
                    courses.append(idx)
                state >>= 1
                idx += 1
            cache[state] = courses
            return courses

        # check - check if the courses of combination can be taken in a semester
        def check(state):
            courses = getCourses(state)

            # make sure at most k courses can be taken
            if len(courses) > k:
                return False
            elif len(courses) == 1:
                return True

            # make sure no prerequisite existed
            for course in courses:
                if course in dicts:
                    return False
            return True

        # check dependency
        cache2 = defaultdict(bool)
        def checkDependence(pre_state, suc_state):
            key = "{}-{}".format(pre_state, suc_state)
            if key in cache2:
                return cache2[key]

            suc_courses = getCourses(suc_state)
            if len(suc_courses) > k:
                cache2[key] = False
                return False

            for suc_course in suc_courses:
                if suc_course in pre_states:
                    if pre_state & pre_states[suc_course] != pre_states[suc_course]:
                        cache2[key] = False
                        return False
            cache2[key] = True
            return True

        # dp init
        # dp[state] - minimal number of semesters to take all course of combination state
        dp = [float("inf")] * L
        for state in range(L):
            if check(state):
                dp[state] = 1
        dp[0] = 0

        # dp transfer
        # dp[state] = min(dp[state] + dp[subset] + dp[state - subset])

        for state in range(L):
            pre_state = state
            while pre_state:
                suc_state = state - pre_state
                if checkDependence(pre_state, suc_state):
                    dp[state] = min(dp[state], dp[pre_state] + 1)
                pre_state = (pre_state - 1) & state
        # print(dp)
        ans = dp[L - 1]
        return ans


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

solution = Solution()
print(solution.minNumberOfSemesters(n, relations, k))
