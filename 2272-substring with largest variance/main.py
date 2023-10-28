class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(list)

        for idx, ch in enumerate(s):
            dicts[ch].append(idx)

        # enumerate maximum difference of subarray for the combination of key and key2
        ans = 0
        for key in dicts:
            for key2 in dicts:
                # key for the max frequent ch and key2 for the min frequent ch
                if key == key2:
                    continue

                idx, idx2 = 0, 0
                f = 0
                g = float("-inf")

                while idx < len(dicts[key]) and idx2 < len(dicts[key2]):
                    if dicts[key][idx] < dicts[key2][idx2]:
                        f = max(f, 0) + 1
                        g += 1
                        idx += 1
                    elif dicts[key][idx] > dicts[key2][idx2]:
                        g = max(f, g, 0) - 1
                        f = max(f, 0) - 1
                        idx2 += 1
                    ans = max(ans, g)

                if idx < len(dicts[key]):
                    for _ in range(idx, len(dicts[key])):
                        f = max(f, 0) + 1
                        g += 1
                        ans = max(ans, g)
                else:
                    ans = max(ans, max(f, g, 0) - 1)

        return ans


s = "aababbb"
#s = "abcde"
#s = "aaaaabbabbbbbbbbabbabbbbbba"
s = "bbc"

solution = Solution()
print(solution.largestVariance(s))


