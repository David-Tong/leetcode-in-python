class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # pre-process
        if x == y:
            return 0

        # process
        from collections import deque
        bfs = deque()
        bfs.append(x)
        visited = set()
        visited.add(x)

        # helper function
        funcs = list()
        # step 1 : divide by 11
        funcs.append(lambda x: x // 11 if x % 11 == 0 else -1)
        # step 2 : divide by 5
        funcs.append(lambda x: x // 5 if x % 5 == 0 else -1)
        # step 3 : decrease by 1
        funcs.append(lambda x: x - 1)
        # step 4: increase by 1
        funcs.append(lambda x: x + 1)
        def process(curr, func):
            nxt = func(curr)
            if nxt == -1:
                return True
            if nxt == y:
                return False
            else:
                if nxt not in visited:
                    visited.add(nxt)
                    bfs.append(nxt)
                return True

        steps = 1
        while bfs:
            size = len(bfs)
            for _ in range(size):
                curr = bfs.popleft()
                for func in funcs:
                    if not process(curr, func):
                        return steps
            steps += 1


x = 26
y = 1

"""
x = 54
y = 2

x = 25
y = 30
"""

solution = Solution()
print(solution.minimumOperationsToMakeEqual(x, y))
