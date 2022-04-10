class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        N = len(words[0])
        M = len(words)

        from collections import defaultdict
        words_dicts = defaultdict(int)
        for word in words:
            words_dicts[word] += 1

        ans = set()
        for x in range(0, len(s) - M * N + 1):
            count = 0
            dicts = defaultdict(int)
            left = x
            right = x
            while right < len(s):
                word = s[right:right + N]
                if word in words_dicts:
                    dicts[word] += 1
                    if dicts[word] <= words_dicts[word]:
                        count += 1
                    else:
                        break
                    if count == M:
                        ans.add(left)
                        break
                    right += N
                else:
                   break
        return ans


s = "barfoothefoobarman"
words = ["foo","bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

#s = "barfoofoobarthefoobarman"
#words = ["bar","foo","the"]

#s = "wordgoodgoodgoodbestword"
#words = ["word","good","best","good"]
#words = []

#s = "aaaaaaaaaaaaaa"
#words = ["aa","aa"]

solution = Solution()
print(solution.findSubstring(s, words))
