class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in s:
            # push
            if stack:
                if ch == stack[-1][0]:
                    stack.append((ch, stack[-1][1] + 1))
                else:
                    stack.append((ch, 1))
            else:
                stack.append((ch, 1))

            # pop
            if stack[-1][1] == k:
                for x in range(k):
                    stack.pop()

        ans = ""
        for ch, num in stack:
            ans += ch
        return ans


s = "abcd"
k = 2

s = "deeedbbcccbdaa"
k = 3

s = "pbbcggttciiippooaais"
k = 2

s = "a"
k = 1

s = "bb"
k = 1

solution = Solution()
print(solution.removeDuplicates(s, k))
