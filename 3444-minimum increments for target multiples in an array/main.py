class Solution(object):
    def minimumIncrements(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        # pre-process
        nums = [0] + nums
        N = len(nums)
        M = len(target)
        L = 2 ** M

        # helper function
        # gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # lcm
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        # cost - the minimum incremets for nums[x] to be target multiplier of a subset
        def cost(num, subset):
            if subset == 0:
                return 0
            l = 1
            idx = 0
            while subset:
                if subset & 1:
                    l = lcm(l, target[idx])
                idx += 1
                subset >>= 1
            res = 0 if num % l == 0 else l - num % l
            return res

        # dp init
        # dp[x][y] - the minimum increments for y combination of target multiplies in array nums[:x + 1]
        dp = [[float("inf")] * L for _ in range(N)]
        for state in range(L):
            dp[0][state] = float("inf")
        dp[0][0] = 0

        # dp transfer
        # condition 1 : nums[x] is not eligible
        #               dp[x][state] = dp[x - 1][state]
        # condition 2: nums[x] is eligible to be multiple of subset from state
        #              for (subset : state)
        #                dp[x][state] = dp[x - 1][state - subset] + cost(nums[x], subset)
        for x in range(1, N):
            for state in range(L):
                dp[x][state] = dp[x - 1][state]
                subset = state
                while subset:
                    dp[x][state] = min(dp[x][state], dp[x - 1][state - subset] + cost(nums[x], subset))
                    subset = (subset - 1) & state
        # print(dp)
        ans = dp[N - 1][L- 1]
        return ans


nums = [1,2,3]
target = [4]

nums = [8,4]
target = [10,5]

nums = [7,9,10]
target = [7]

from random import randint
nums = list()
for x in range(5 * 10 ** 4):
    nums.append(randint(1, 10000))
target = [5480, 9819, 6781]

solution = Solution()
print(solution.minimumIncrements(nums, target))
