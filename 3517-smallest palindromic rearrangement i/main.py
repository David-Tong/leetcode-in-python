class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        # process
        ans = ""
        middle = ""
        for ch in sorted(dicts.keys()):
            if dicts[ch] % 2 == 0:
                ans += ch * (dicts[ch] // 2)
            else:
                ans += ch * (dicts[ch] // 2)
                middle = ch
        reverse = ans[::-1]
        ans = ans + middle + reverse
        return ans


s = "z"
s = "babab"
s = "daccad"

solution = Solution()
print(solution.smallestPalindrome(s))
