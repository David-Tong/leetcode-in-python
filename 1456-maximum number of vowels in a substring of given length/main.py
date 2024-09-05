class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L = len(s)

        # init
        vowels = 0
        for x in range(k):
            if s[x] in "aeiou":
                vowels += 1

        ans = vowels
        index = 1
        while index + k <= L:
            if s[index - 1] in "aeiou":
                vowels -= 1
            if s[index + k - 1] in "aeiou":
                vowels += 1
            ans = max(ans, vowels)
            index += 1
        return ans


s = "abciiidef"
k = 3

s = "aeiou"
k = 2

s = "leetcode"
k = 3

s = "aexxxxxxaei"
k = 3

s = "aeexxxxxxaez"
k = 3

solution = Solution()
print(solution.maxVowels(s, k))
