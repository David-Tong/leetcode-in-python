class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # pre-process
        MOD = n - 1
        if ((time - 1) // MOD) % 2 == 0:
            direction = True
        else:
            direction = False

        offset = time % MOD
        if offset == 0:
            offset = MOD

        # process
        ans = 0
        if direction:
            ans = 1 + offset
        else:
            ans = n - offset
        return ans


n = 4
time = 5

n = 3
time = 2

n = 3
time = 1

solution = Solution()
print(solution.passThePillow(n, time))
