class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = len(word)

        # helper function
        def distance(ch, ch2):
            if ch > ch2:
                ch, ch2 = ch2, ch
            return min(ord(ch2) - ord(ch), ord(ch) + 26 - ord(ch2))

        # process
        ans = L
        prev = 'a'
        for ch in word:
            ans += distance(prev, ch)
            prev = ch
        return ans


word = "abc"
word = "bza"
word = "zjpc"

solution = Solution()
print(solution.minTimeToType(word))
