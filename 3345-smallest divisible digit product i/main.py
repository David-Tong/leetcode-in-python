class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        # pre-process
        # helper function
        def divisible(n):
            product = 1
            for d in str(n):
                product *= int(d)
            return product % t == 0

        # process
        idx = n
        while not divisible(idx):
            idx += 1
        ans = idx
        return ans


n = 10
t = 2

n = 15
t = 3

solution = Solution()
print(solution.smallestNumber(n, t))


