class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # dp[x] - max sum of a legal subsequence
        dp = [0] * L

        from collections import deque
        queue = deque()

        # transfer
        for x in range(L):
            if queue:
                dp[x] = max(0, queue[0]) + nums[x]
            else:
                dp[x] = nums[x]
            while queue and queue[-1] < dp[x]:
                queue.pop()
            queue.append(dp[x])

            if x - k >= 0:
                if queue[0] == dp[x - k]:
                    queue.popleft()

        return max(dp)


nums = [10,2,-10,5,20]
k = 2

nums = [-1,-2,-3]
k = 1

nums = [10,-2,-10,-5,20]
k = 2

nums = [10,3,-2,-5,-7,11,3,-5,-1,12,-1,-3,12]
k = 2

nums = [-3]
k = 1

nums = [-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790]
k = 1

solution = Solution()
print(solution.constrainedSubsetSum(nums, k))
