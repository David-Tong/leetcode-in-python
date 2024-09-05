class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        L = len(num)

        maxi = -1
        for x in range(L - 2):
            if num[x] == num[x + 1] == num[x + 2]:
                maxi = max(maxi, num[x])

        if maxi == -1:
            return ""
        else:
            return str(maxi) * 3


num = "6777133339"
num = "2300019"
num = "42352338"

solution = Solution()
print(solution.largestGoodInteger(num))
