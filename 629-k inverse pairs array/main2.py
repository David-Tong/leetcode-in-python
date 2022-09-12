class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def swap(left, right, curr):
            return curr[:left] + curr[right] + curr[left+1:right] + curr[left] + curr[right+1:]

        nums = "".join([str(_ + 1) for _ in range(n)])

        from collections import deque
        bfs = deque()
        bfs.append(nums)
        visited = set()
        visited.add(nums)

        idx = 0
        while bfs and idx <= k:
            L = len(bfs)
            if idx == k:
                return L
            for x in range(L):
                curr = bfs.popleft()
                stack = list()
                for x in range(n):
                    while stack and int(stack[-1][1]) < int(curr[x]):
                        item = stack.pop()
                        left = item[0]
                        right = x
                        next = swap(left, right, curr)
                        if next not in visited:
                            bfs.append(next)
                            visited.add(next)
                    stack.append((x, curr[x]))
            idx += 1

        return 0


n = 3
k = 3

solution = Solution()
print(solution.kInversePairs(n, k))
