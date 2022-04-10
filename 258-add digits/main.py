class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def doAddDigits(num):
            sums = 0
            sums += num % 10
            num = num // 10
            while num > 0:
                sums += num % 10
                num = num // 10
            return sums

        while num >= 10:
            num = doAddDigits(num)
        return num


num = 38
num = 0
num = 11111111111111111111

solution = Solution()
print(solution.addDigits(num))
