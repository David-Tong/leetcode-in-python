class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 1
        step = 0
        while right + step < len(s):
            if s[left + step] < s[right + step]:
                left = right
                right += 1
                step = 0
            elif s[left + step] == s[right + step]:
                step += 1
            else:
                right += 1
                step = 0

        return s[left:]


s = "abab"
s = "leetcode"
s = "zrziy"

solution = Solution()
print(solution.lastSubstring(s))
