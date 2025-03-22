class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # pre-process
        L = len(s)
        left, right = 0, L

        # process
        ans = list()
        for ch in s:
            if ch == "I":
                ans.append(left)
                left += 1
            elif ch == "D":
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans


s = "IDID"
s = "III"
s = "DDI"

solution = Solution()
print(solution.diStringMatch(s))
