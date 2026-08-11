class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # pre-process
        # helper function
        def waviness(num):
            s = str(num)
            L = len(s)
            if L < 3:
                return 0

            res = 0
            for i in range(1, L - 1):
                a = int(s[i - 1])
                b = int(s[i])
                c = int(s[i + 1])

                if b > a and b > c:
                    res += 1
                elif b < a and b < c:
                    res += 1

            return res

        # process
        ans = 0
        for num in range(num1, num2 + 1):
            ans += waviness(num)
        return ans


num1 = 120
num2 = 130

num1 = 198
num2 = 202

num1 = 4848
num2 = 4848

solution = Solution()
print(solution.totalWaviness(num1, num2))
