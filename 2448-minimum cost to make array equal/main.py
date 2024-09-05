class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(nums)

        # pre-process
        pairs = zip(nums, cost)
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

        # pre-sum
        presums = [0] * (N + 1)
        for x in range(N):
            presums[x + 1] += presums[x] + pairs[x][1]

        left_cost = 0
        right_cost = 0
        for x in range(1, N):
            right_cost += (pairs[x][0] - pairs[0][0]) * pairs[x][1]

        # search
        ans = float("inf")
        for x in range(N):
            if x == 0:
                pass
            else:
                left_cost += presums[x] * (pairs[x][0] - pairs[x - 1][0])
                right_cost -= (presums[N] - presums[x]) * (pairs[x][0] - pairs[x - 1][0])
            ans = min(ans, left_cost + right_cost)
        return ans


nums = [1,3,5,2]
cost = [2,3,1,14]

nums = [2,2,2,2,2]
cost = [4,2,8,1,3]

nums = [1,4,5,6,7,8,2,11]
cost = [2,4,5,6,7,8,1,2]

nums = [4,10]
cost = [2,1]

solution = Solution()
print(solution.minCost(nums, cost))
