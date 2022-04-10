class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        N = len(num1)
        M = len(num2)
        ans = [0] * (N + M)
        for x in range(N, 0, -1):
            for y in range(M, 0, -1):
                product = (int(num1[x-1])) * (int(num2[y-1])) + ans[x + y - 1]
                ans[x + y - 1] = product % 10
                ans[x + y - 2] += product // 10

        ans = [str(_) for _ in ans]
        idx = 0
        while idx < len(ans) and ans[idx] == "0":
            idx += 1
        return "".join(ans[idx:]) if idx < len(ans) else "0"


num1 = "2"
num2 = "3"

num1 = "123"
num2 = "456"

num1 = "999"
num2 = "999"

#num1 = "0"
#num2 = "0"

solution = Solution()
print(solution.multiply(num1, num2))
