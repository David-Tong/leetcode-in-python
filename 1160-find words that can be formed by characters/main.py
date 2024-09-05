class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for char in chars:
            dicts[char] += 1

        # process
        ans = 0
        for word in words:
            word_dicts = defaultdict(int)
            for char in word:
                word_dicts[char] += 1
            has = True
            for key in word_dicts:
                if word_dicts[key] > dicts[key]:
                    has = False
                    break
            if has:
                ans += len(word)
        return ans


words = ["cat","bt","hat","tree"]
chars = "atach"

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

solution = Solution()
print(solution.countCharacters(words, chars))
