class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseString(s, ans, left, right):
            index = right
            while index >= left:
                ans += s[index]
                index -= 1
            return ans

        left = 0
        right = 0
        ans = ""
        while right < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            ans = reverseString(s, ans, left, right - 1)
            if right < len(s):
                ans += s[right]
            right += 1
            left = right

        return ans


solution = Solution()
s = "Let's take LeetCode contest"
s = "God Ding"
s = "A"
print(solution.reverseWords(s))