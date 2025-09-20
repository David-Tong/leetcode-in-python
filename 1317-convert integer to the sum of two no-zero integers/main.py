class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # process
        for x in range(1, n):
            if str(x).count('0') == 0:
                other = n - x
                if str(other).count('0') == 0:
                    ans = [x, other]
                    return ans
        return None


n = 2
n = 11
n = 111
n = 4102

solution = Solution()
print(solution.getNoZeroIntegers(n))
