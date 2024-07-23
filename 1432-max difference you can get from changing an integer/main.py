class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        maxi, mini = num, num

        for digit in num:
            if digit != "9":
                maxi = num.replace(digit, "9")
                break

        for idx, digit in enumerate(num):
            if digit != "1" and digit != "0":
                if idx == 0:
                    mini = num.replace(digit, "1")
                else:
                    mini = num.replace(digit, "0")
                break

        print(maxi, mini)
        ans = int(maxi) - int(mini)
        return ans


num = 555
num = 9
num = 57328462
num = 11111
num = 99999
num = 10000
num = 38423847
num = 123456
num = 9876543
num = 1101057

solution = Solution()
print(solution.maxDiff(num))
