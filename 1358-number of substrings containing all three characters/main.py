class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        count = 0
        ans = 0
        # slow-fast pointer
        fast = 0
        for slow in range(L):
            while fast < L and count < 3:
                ch = s[fast]
                if dicts[ch] == 0:
                    count += 1
                dicts[ch] += 1
                fast += 1

            # condition met
            if count == 3:
                ans += L - fast + 1

            ch = s[slow]
            if dicts[ch] == 1:
                count -= 1
            dicts[ch] -= 1

        return ans


s = "abcabc"
s = "aaacb"
s = "abc"

solution = Solution()
print(solution.numberOfSubstrings(s))
