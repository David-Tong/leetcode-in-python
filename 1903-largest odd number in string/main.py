class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        L = len(num)

        idx = L - 1
        while idx >= 0:
            if int(num[idx]) % 2 == 0:
                idx -= 1
            else:
                break

        return num[:idx + 1]


num = "52"
num = "4206"
num = "35427"

solution = Solution()
print(solution.largestOddNumber(num))
