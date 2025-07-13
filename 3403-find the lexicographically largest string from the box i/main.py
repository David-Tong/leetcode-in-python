class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        # short-cut
        if numFriends == 1:
            return word

        # pre-process
        L = len(word)
        maxi = 'a'
        for ch in word:
            maxi = max(maxi, ch)

        # process
        l = L - (numFriends - 1)
        matched = list()
        for start, ch in enumerate(word):
            if maxi == ch:
                end = min(L, start + l)
                matched.append(word[start: end])
        matched = sorted(matched)
        ans = matched[-1]
        return ans


word = "dbca"
numFriends = 2

word = "gggg"
numFriends = 4

word = "zaazb"
numFriends = 2

word = "gh"
numFriends = 1

solution = Solution()
print(solution.answerString(word, numFriends))
