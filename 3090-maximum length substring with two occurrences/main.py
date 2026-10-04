class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        ans = 0
        left = 0
        right = 0
        while right < L:
            ch = s[right]
            dicts[ch] += 1

            while dicts[ch] > 2:
                ch2 = s[left]
                dicts[ch2] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans


s = "bcbbbcba"
s = "aaaa"
s = "ababab"

solution = Solution()
print(solution.maximumLengthSubstring(s))
