class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        for word in words:
            dicts[word] += 1

        ans = 0
        center = True
        for word in dicts:
            if word[::-1] in dicts:
                if word[0] == word[1]:
                    if dicts[word] % 2 == 1:
                        if center:
                            ans += 2
                            center = False
                    ans += (dicts[word] // 2) * 4
                else:
                    ans += min(dicts[word], dicts[word[::-1]]) * 2
        return ans


words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
words = ["cc","ll","xx"]
words = ["ab","ty","yt","lc","cl","ab","yt"]
words = ["cc","cc","bb","bb"]
words = ["cc","cc","bb","bb","bb","aa"]

solution = Solution()
print(solution.longestPalindrome(words))
