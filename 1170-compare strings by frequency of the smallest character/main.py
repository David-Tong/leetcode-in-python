class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(word):
            from collections import defaultdict
            dicts = defaultdict(int)
            for ch in word:
                dicts[ch] += 1
            smallest = sorted(dicts.keys())[0]
            return dicts[smallest]

        # pre-process
        queries_result = list()
        for query in queries:
            queries_result.append(f(query))

        words_result = list()
        for word in words:
            words_result.append(f(word))
        words_result = sorted(words_result)
        L = len(words_result)

        # process
        ans = list()
        from bisect import bisect_right
        for query_result in queries_result:
            idx = bisect_right(words_result, query_result)
            ans.append(L - idx)
        return ans


queries = ["cbd"]
words = ["zaaaz"]

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

solution = Solution()
print(solution.numSmallerByFrequency(queries, words))
