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
        # dp init
        # dp[i] - maximum jumps starting from index i
        dp = [1] * L

        # sort indices by arr value (ascending)
        order = sorted(range(L), key=lambda x: arr[x])

        # process from smallest value to largest
        for idx in order:
            # search right
            for step in range(1, d + 1):
                j = idx + step
                if j >= L:
                    break
                # stop if arr[j] is not strictly smaller
                if arr[j] >= arr[idx]:
                    break
                dp[idx] = max(dp[idx], 1 + dp[j])

            # search left
            for step in range(1, d + 1):
                j = idx - step
                if j < 0:
                    break
                # stop if arr[j] is not strictly smaller
                if arr[j] >= arr[idx]:
                    break
                dp[idx] = max(dp[idx], 1 + dp[j])

        # post-process
        return max(dp)


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