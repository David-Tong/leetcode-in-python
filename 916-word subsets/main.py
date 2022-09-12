class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        def matchWord(dict, word1):
            from collections import defaultdict
            dict1 = defaultdict(int)
            for ch in word1:
                dict1[ch] += 1

            for ch in dict:
                    if dict[ch] > dict1[ch]:
                        return False
            return True

        from collections import defaultdict
        dict2 = defaultdict(defaultdict)
        for word2 in words2:
            dict2[word2] = defaultdict(int)
            for ch in word2:
                dict2[word2][ch] += 1

        dict = defaultdict(int)
        for word2 in words2:
            for ch in word2:
                dict[ch] = max(dict[ch], dict2[word2][ch])

        ans = list()
        for word1 in words1:
            if matchWord(dict, word1):
                ans.append(word1)
        return ans


words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["le"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]

solution = Solution()
print(solution.wordSubsets(words1, words2))
