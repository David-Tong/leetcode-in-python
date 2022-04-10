class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        index = 0
        count = k
        while count > 0 and index < len(num):
            while count > 0 and len(stack) > 0 and stack[-1] > num[index]:
                stack.pop(-1)
                count -= 1
            stack.append(num[index])
            index += 1

        while count > 0:
            stack.pop(-1)
            count -= 1

        ans = ""
        for item in stack:
            ans += str(item)
        ans += num[index:]

        index = 0
        while index < len(ans):
            if ans[index] == "0":
                index += 1
            else:
                break
        ans = ans[index:]

        if len(ans) == 0:
            return "0"
        else:
            return ans


num = "1432219"
k = 3

num = "10200"
k = 1

num = "10"
k = 2

num = "12"
k = 2

num = "10001"
k = 1

solution = Solution()
print(solution.removeKdigits(num, k))
