class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        positive = True
        if num < 0:
            positive = False
            num = -1 * num

        mod7 = num % 7
        div7 = num // 7
        ans = ""
        while div7 != 0:
            ans = str(mod7) + ans
            mod7 = div7 % 7
            div7 = div7 // 7
        ans = str(mod7) + ans

        if not positive:
            ans = "-" + ans
        return ans


num = 100
num = -7

solution = Solution()
print(solution.convertToBase7(num))
