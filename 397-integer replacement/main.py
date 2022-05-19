class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        from collections import deque
        bfs = deque()
        bfs.append((n, 0))
        visited = set()
        visited.add(n)
        while bfs:
            curr, steps = bfs.popleft()
            nexts = list()
            if curr % 2 == 0:
                nexts.append(curr / 2)
            else:
                nexts.append(curr + 1)
                nexts.append(curr - 1)

            for next in nexts:
                if next == 1:
                    return steps + 1
                if next not in visited:
                    bfs.append((next, steps + 1))
                    visited.add(next)
        return -1


n = 8
n = 7
n = 4
n = 65000
n = 2147483647

solution = Solution()
print(solution.integerReplacement(n))
