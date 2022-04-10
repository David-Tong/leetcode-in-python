class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
s = "a"

solution = Solution()
print(solution.isPalindrome(s))
