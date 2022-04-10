class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def doLcd(x, y):
            if x < y:
                return doLcd(y, x)
            else:
                if y == 0:
                    return x
                else:
                    return doLcd(y, x % y)

        from collections import defaultdict
        lcds = defaultdict(int)
        ans = 0
        for num in nums:
            lcd = doLcd(num, k)
            for lcd2 in lcds:
                if lcd * lcd2 % k == 0:
                    ans += lcds[lcd2]
            lcds[lcd] += 1
        return ans


nums = [1, 2, 3, 4, 5]
k = 2

nums = [1, 2, 3, 4]
k = 5

nums = [2, 3]
k = 6

solution = Solution()
print(solution.countPairs(nums, k))
