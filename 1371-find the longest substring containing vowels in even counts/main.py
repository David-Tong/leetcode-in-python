class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        VOWELS = "aeiou"
        presums = [[0] * 5 for _ in range(L + 1)]
        from collections import defaultdict
        dicts = defaultdict(int)
        dicts["00000"] = 0

        # process
        ans = 0
        for idx, ch in enumerate(s):
            key = ""
            for idx2, vowel in enumerate("aeiou"):
                presums[idx + 1][idx2] = presums[idx][idx2]
                if ch == vowel:
                    presums[idx + 1][idx2] += 1
                    # encode
                if presums[idx + 1][idx2] % 2 == 1:
                    key = "1" + key
                else:
                    key = "0" + key

            if key not in dicts:
                dicts[key] = idx + 1
            else:
                ans = max(ans, idx + 1 - dicts[key])
        return ans


s = "eleetminicoworoep"
s = "leetcodeisgreat"
s = "bcbcbc"
s = "hsugfueguaabiwhyfueiiuussgaaeefgas"
s = "a"

solution = Solution()
print(solution.findTheLongestSubstring(s))
