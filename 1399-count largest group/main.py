class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        # helper functions
        # get sum of digits
        def getSum(x):
            x = str(x)
            total = 0
            for digit in x:
                total += int(digit)
            return total

        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        for x in range(1, n + 1):
            total = getSum(x)
            dicts[total] += 1
        # print(dicts)

        # post-process
        maxi = max(dicts.values())
        ans = 0
        for key in dicts:
            if dicts[key] == maxi:
                ans += 1
        return ans


n = 13
n = 2
n = 10000

solution = Solution()
print(solution.countLargestGroup(n))
