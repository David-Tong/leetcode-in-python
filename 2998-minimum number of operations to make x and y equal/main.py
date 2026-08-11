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
        def process(nxt):
            if nxt not in visited:
                visited.add(nxt)
                bfs.append(nxt)

        steps = 1
        while bfs:
            size = len(bfs)
            for _ in range(size):
                curr = bfs.popleft()
                # step 1 : divide by 11
                if curr % 11 == 0:
                    nxt = curr // 11
                    if nxt == y:
                        return steps
                    process(nxt)
                # step 2 : divide by 5
                if curr % 5 == 0:
                    nxt = curr // 5
                    if nxt == y:
                        return steps
                    process(nxt)
                # step 3 : decrease by 1
                if curr > 0:
                    nxt = curr - 1
                    if nxt == y:
                        return steps
                    process(nxt)
                # step 4: increase by 1
                nxt = curr + 1
                if nxt == y:
                    return steps
                process(nxt)
            steps += 1


x = 26
y = 1

x = 54
y = 2

x = 25
y = 30

solution = Solution()
print(solution.minimumOperationsToMakeEqual(x, y))
