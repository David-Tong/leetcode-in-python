class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        STEP = 4
        # helper function
        def isPunishmentNumber(s, num, total):
            if len(s) == 0:
                if num == total:
                    return True
                else:
                    return False

            for x in range(STEP):
                part = int(s[:x + 1])
                if isPunishmentNumber(s[x + 1:], num, total + part):
                    return True
            return False

        # process
        ans = 0
        for x in range(n):
            num = (x + 1) ** 2
            if isPunishmentNumber(str(num), x + 1, 0):
                ans += num
        return ans


solution = Solution()

n = 10
n = 37
n = 1000
print(solution.punishmentNumber(n))