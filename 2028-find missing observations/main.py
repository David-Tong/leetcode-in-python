class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        # pre-process
        M = len(rolls)
        total = sum(rolls)
        remain = mean * (M + n) - total
        if 1 * n <= remain <= 6 * n:
            pass
        else:
            return list()

        # process
        average = remain // n
        addon = remain % n
        ans = list()
        for x in range(n):
            ans.append(average)
        for x in range(addon):
            ans[x] += 1
        return ans


rolls = [3,2,4,3]
mean = 4
n = 2

rolls = [1,5,6]
mean = 3
n = 4

rolls = [1,2,3,4]
mean = 6
n = 4

solution = Solution()
print(solution.missingRolls(rolls, mean, n))

