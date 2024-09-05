class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        def gcd(x, y):
            if x % y == 0:
                return y
            else:
                return gcd(y, x % y)

        def doScore(selected):
            key = "-".join([str(_) for _ in sorted(selected)])
            if key in self.cache:
                return self.cache[key]

            if len(selected) == N:
                return 0

            score = 0
            for x in range(N):
                for y in range(x + 1, N):
                    if x not in selected and y not in selected:
                        i = len(selected) // 2 + 1
                        score = max(score, i * gcds[x][y] + doScore(selected + [x, y]))
            self.cache[key] = score
            return score

        nums = sorted(nums)
        gcds = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(x + 1, N):
                gcds[x][y] = gcd(nums[x], nums[y])

        from collections import defaultdict
        self.cache = defaultdict(int)

        return doScore(list())


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
