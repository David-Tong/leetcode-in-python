class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        N = len(s)
        M = s.count('0')

        # short-cuts
        if M == 0:
            return 0

        if M % 2 == 1 and k % 2 == 0:
            return -1

        from sortedcontainers import SortedList
        evens_not_visited = SortedList(range(0, N + 1, 2))
        odds_not_visited = SortedList(range(1, N + 1, 2))
        evens_not_visited.add(N + 1)
        odds_not_visited.add(N + 1)

        # helper function
        def get_not_visited(curr):
            return evens_not_visited if curr % 2 == 0 else odds_not_visited

        # process
        start = M

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(start)
        not_visited = get_not_visited(start)
        not_visited.discard(start)

        ans = 0
        while bfs:
            size = len(bfs)
            for _ in range(size):
                curr = bfs.popleft()
                if curr == 0:
                    return ans

                # mini and maxi number of zeros can be reached after one operation
                mini = curr + k - 2 * min(k, curr)
                maxi = curr + k - 2 * max(0, k - N + curr)
                # the next reach point must be even or odd number only
                not_visited = get_not_visited(mini)
                idx = not_visited.bisect_left(mini)
                while not_visited[idx] <= maxi:
                    nxt = not_visited.pop(idx)
                    bfs.append(nxt)
            ans += 1
        return -1


s = "110"
k = 1

s = "0101"
k = 3

s = "101"
k = 2

import random
s = "".join([random.choice("01") for _ in range(10 ** 4)])
k = 1000
print(s)

solution = Solution()
print(solution.minOperations(s, k))
