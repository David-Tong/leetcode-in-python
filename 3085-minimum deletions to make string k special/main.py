class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in word:
            dicts[ch] += 1
        counts = defaultdict(int)
        for ch in dicts:
            counts[dicts[ch]] += 1
        # print(counts)

        # process
        keys = sorted(counts.keys())
        L = len(keys)
        from bisect import bisect_right
        ans = float("inf")
        left = 0
        for x in range(L):
            target = keys[x] + k
            idx = bisect_right(keys, target)
            right = 0
            for y in range(idx, L):
                right += (keys[y] - target) * counts[keys[y]]
            ans = min(ans, left + right)
            left += keys[x] * counts[keys[x]]
        return ans


word = "aabcaba"
k = 0

word = "dabdcbdcdcd"
k = 2

word = "aaabaaa"
k = 2

solution = Solution()
print(solution.minimumDeletions(word, k))
