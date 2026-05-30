class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        # pre-process
        L = len(arr)

        # process
        # memorized dfs
        from collections import defaultdict
        memo = defaultdict(int)  # 0 means "not computed yet"

        def dfs(idx):
            # use cache
            if memo[idx] != 0:
                return memo[idx]

            best = 1  # At least the current index is counted

            # search the right
            for step in range(1, d + 1):
                j = idx + step
                if j >= L:
                    break
                # stop if arr[j] is not strictly smaller than arr[i]
                if arr[j] >= arr[idx]:
                    break
                best = max(best, 1 + dfs(j))

            # search the left
            for step in range(1, d + 1):
                j = idx - step
                if j < 0:
                    break
                # same stopping rule as the right side
                if arr[j] >= arr[idx]:
                    break
                best = max(best, 1 + dfs(j))

            memo[idx] = best
            return best

        # post process
        result = 0
        for idx in range(0, L):
            result = max(result, dfs(idx))

        return result


arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2

arr = [3,3,3,3,3]
d = 3

arr = [7,6,5,4,3,2,1]
d = 1

from random import randint
arr = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
d = 10 ** 3
print(arr)

solution = Solution()
print(solution.maxJumps(arr, d))
