class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        L = len(text)
        from collections import defaultdict
        dict = defaultdict(list)

        left = 0
        right = 0
        while right < L:
            curr = text[right]
            if text[left] != curr:
                dict[text[left]].append((left, right - 1))
            while text[left] != curr:
                left += 1
            right += 1
        dict[text[left]].append((left, right - 1))

        ans = 0
        for ch in dict:
            for idx in range(len(dict[ch])):
                if idx < len(dict[ch]) - 1:
                    if dict[ch][idx][1] + 2 == dict[ch][idx + 1][0]:
                        if len(dict[ch]) > 2:
                            ans = max(ans, dict[ch][idx + 1][1] - dict[ch][idx][0] + 1)
                        else:
                            ans = max(ans, dict[ch][idx + 1][1] - dict[ch][idx][0])
                if len(dict[ch]) > 1:
                    ans = max(ans, dict[ch][idx][1] - dict[ch][idx][0] + 2)
                else:
                    ans = max(ans, dict[ch][idx][1] - dict[ch][idx][0] + 1)
        return ans


text = "ababa"
text = "aaabaaa"
text = "aaaaa"
text = "aaabbaaa"

solution = Solution()
print(solution.maxRepOpt1(text))
