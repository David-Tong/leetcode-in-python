class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(bool)
        for root in dictionary:
            dicts[root] = True

        # process
        ans = ""
        for word in sentence.split():
            for x in range(len(word)):
                key = word[:x + 1]
                if key in dicts:
                    ans += key + " "
                    break
            else:
                ans += word + " "
        return ans[:-1]


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"

solution = Solution()
print(solution.replaceWords(dictionary, sentence))
