class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "aeiou" + "AEIOU"

        vowels = list()
        positions = list()
        for idx, ch in enumerate(s):
            if ch in VOWELS:
                vowels.append(ch)
                positions.append(idx)
        positions = [-1] + positions + [len(s)]

        ans = ""
        for x in range(len(positions) - 1):
            start = positions[x] + 1
            end = positions[x + 1]
            if x == len(positions) - 2:
                ans += s[start:end]
            else:
                ans += s[start:end] + vowels[-1 - x]
        return ans


s = "hello"
s = "leetcode"
s = "aeiou"
s = "LeetcOdE"

solution = Solution()
print(solution.reverseVowels(s))
