class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        self.cache = defaultdict(int)

        # helper function
        def step(num):
            key = "{}".format(num)
            if key in self.cache:
                return self.cache[key]
            if num == 1:
                return 0

            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            res = step(num) + 1
            self.cache[key] = res
            return res

        # process
        steps = list()
        for num in range(lo, hi + 1):
            steps.append((step(num), num))
        steps = sorted(steps)
        ans = steps[k - 1][1]
        return ans


lo = 12
hi = 15
k = 2

lo = 7
hi = 11
k = 4

lo = 50
hi = 50
k = 1

lo = 1
hi = 1000
k = 500

solution = Solution()
print(solution.getKth(lo, hi, k))
