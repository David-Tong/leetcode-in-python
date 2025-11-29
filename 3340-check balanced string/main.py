class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # pre-process
        L = len(num)

        # process
        half, total = 0, 0
        for x in range(L):
            if x % 2 == 0:
                half += int(num[x])
            total += int(num[x])

        return total - half == half


num = "1234"
num = "24123"

solution = Solution()
print(solution.isBalanced(num))
