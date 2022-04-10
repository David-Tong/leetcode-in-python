class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def doReplacement(s, k, ch):
            from collections import defaultdict
            dicts = defaultdict(int)

            left = 0
            right = 0
            ans = 0
            while right < len(s):
                dicts[s[right]] += 1
                while right - left + 1 - dicts[ch] > k:
                    dicts[s[left]] -= 1
                    if dicts[s[left]] == 0:
                        del dicts[s[left]]
                    left += 1
                ans = max(ans, right - left + 1)
                right += 1
            return ans

        import string
        ans = 0
        for ch in string.ascii_uppercase:
            ans = max(ans, doReplacement(s, k, ch))
        return ans


s = "ABAB"
k = 2

s = "AABABBA"
k = 1

solution = Solution()
print(solution.characterReplacement(s, k))
