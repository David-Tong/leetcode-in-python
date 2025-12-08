class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(nums)

        # dp init
        # dp[idx] - the number of partitions with max-min difference at most k for nums[:idx]
        dp = [0] * (L + 1)
        dp[0] = 1
        presums = list()
        presums.append(0)
        presums.append(dp[0])

        # dp transfer
        # dp[idx] = sum(dp[idx2], ..., dp[idx - 1])
        # idx2 - the beginning of subarray with max-min difference at most k
        from sortedcontainers import SortedList
        sl = SortedList()

        idx, idx2 = 0, 0
        while idx < L:
            sl.add(nums[idx])
            max_min = sl[-1] - sl[0]
            while max_min > k:
                sl.remove(nums[idx2])
                max_min = sl[-1] - sl[0]
                idx2 += 1
            dp[idx + 1] = (presums[idx + 1] - presums[idx2]) % MODULO
            presums.append((presums[-1] + dp[idx + 1]) % MODULO)
            idx += 1

        ans = dp[L] % MODULO
        return ans


nums = [9,4,1,3,7]
k = 4

nums = [3, 3, 4]
k = 0

from random import randint
nums = [randint(1, 10 ** 3) for _ in range(5 * 10 ** 4)]
k = 350
print(nums)

solution = Solution()
print(solution.countPartitions(nums, k))
