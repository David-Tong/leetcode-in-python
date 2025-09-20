class Solution(object):
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # dp init
        # dp[x][y] - the number of sequence with length of y and ended with nums[x]
        dp = [[0] * (k + 1) for _ in range(L)]
        for x in range(L):
            dp[x][1] = 1
        total = [0] * (k + 1)
        total[1] = 1

        # dp transfer
        # dp[x][y] = sum of dp[z][y -1] for z from 0 to x - 1
        # dp[x][y] = total[y - 1]
        for x in range(1, L):
            for y in range(k):
                dp[x][y + 1] += total[y]
            for y in range(k):
                total[y + 1] += dp[x][y + 1]

        # print(dp)
        # print(total)

        # process
        MODULO = 10 ** 9 + 7
        nums = sorted(nums)
        mini, maxi = 0, 0
        for x in range(L):
            s = sum(dp[x])
            mini = (mini + s * nums[L - 1 - x]) % MODULO
            maxi = (maxi + s * nums[x]) % MODULO

        ans = (mini + maxi) % MODULO
        return ans


nums = [1,2,3]
k = 2

nums = [1,2,3,4]
k = 4

nums = [5,0,6]
k = 1

nums = [1,1,1]
k = 2

nums = [10,5,9,9,10,10,7,7,9,6,9,6,7,6,4,9,8,4,2,0,0,3,9,3,10,3,1,9,8,2,8,2,0,7,7,6,4,6,7,3,2,5,6,6,5,0,5,7,8,1]
k = 29

solution = Solution()
print(solution.minMaxSums(nums, k))
