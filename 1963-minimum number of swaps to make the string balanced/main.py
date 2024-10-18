class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # two pointers
        left, right = 0, L - 1
        balance = 0
        ans = 0

        # process
        while left < right:
            if s[left] == "[":
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    balance += 2
                    ans += 1
                    right -= 1
            left += 1
        return ans


s = "][]["
s = "]]][[["
s = "[]"
s = "]][]][[[][][]["

solution = Solution()
print(solution.minSwaps(s))
