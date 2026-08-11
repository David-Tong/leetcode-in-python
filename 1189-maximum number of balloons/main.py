from compiler.transformer import k


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in text:
            dicts[ch] += 1

        # process
        KEYS = "banlo"
        ans = float('inf')
        for key in KEYS:
            if key in "ban":
                if dicts[key] > 0:
                    ans = min(ans, dicts[key])
                else:
                    return 0
            elif key in "lo":
                if dicts[key] > 1:
                    ans = min(ans, dicts[key] // 2)
                else:
                    return 0
        return ans


text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"
text = "lloo"

solution = Solution()
print(solution.maxNumberOfBalloons(text))
