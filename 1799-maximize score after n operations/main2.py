class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        from collections import defaultdict
        self.cache = defaultdict(int)

        def gcd(x, y):
            if x % y == 0:
                return y
            else:
                return gcd(y, x % y)

        def doScore(mask, i):
            if mask in self.cache:
                return self.cache[mask]

            if i == N // 2 + 1:
                return 0

            score = 0
            for x in range(N):
                for y in range(x + 1, N):
                    if mask & (1 << x) == 0 and mask & (1 << y) == 0:
                        new_mark = mask ^ (1 << x) ^ (1 << y)
                        score = max(score, i * gcds[x][y] + doScore(new_mark, i + 1))
            self.cache[mask] = score
            return score

        nums = sorted(nums)
        gcds = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(x + 1, N):
                gcds[x][y] = gcd(nums[x], nums[y])

        return doScore(0, 1)


nums = [1,2]
nums = [3,4,6,8]
nums = [1,2,3,4,5,6]
nums = [100,34,56789,13435]
nums = [100,34,56789,13435,131241,945,35632,45678,121231,23,19,13,33,131241]
nums = [415,230,471,705,902,87]
nums = [18972,164591,210610,899193,343662,850541,590706,820721,141708,355568,450092,223378,279483,707218]
nums = [9,17,16,15,18,13,18,20]

solution = Solution()
print(solution.maxScore(nums))
