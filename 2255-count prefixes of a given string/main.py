class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        # pre-process
        # helper function
        def isPrefix(word, s):
            idx = 0
            if len(word) > len(s):
                return False

            while idx < len(word):
                if word[idx] == s[idx]:
                    idx += 1
                else:
                    return False
            return True

        # process
        ans = 0
        for word in words:
            if isPrefix(word, s):
                ans += 1
        return ans


words = ["a","b","c","ab","bc","abc"]
s = "abc"

words = ["a","a"]
s = "aa"

words = ["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"]
s = "w"

solution = Solution()
print(solution.countPrefixes(words, s))
