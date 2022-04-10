class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def decode(num):
            return chr(ord('a') + int(num) - 1)

        ans = ""
        idx = 0
        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == "#":
                ans += decode(s[idx:idx+2])
                idx += 3
            else:
                ans += decode(s[idx:idx+1])
                idx += 1
        return ans


s = "10#11#12"
s = "1326#"
s = "3"

solution = Solution()
print(solution.freqAlphabets(s))
