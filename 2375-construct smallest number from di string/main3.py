class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        # pre-process
        L = len(pattern) + 1

        # process
        stack = list()
        ans = ""

        for x in range(L):
            stack.append(str(x + 1))
            if x == L - 1 or pattern[x] == "I":
                while stack:
                    ans += stack.pop()
        return ans


pattern = "IIIDIDDD"

solution = Solution()
print(solution.smallestNumber(pattern))
