class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            ans += 1
        return ans


num = 14
num = 8
num = 123

solution = Solution()
print(solution.numberOfSteps(num))
