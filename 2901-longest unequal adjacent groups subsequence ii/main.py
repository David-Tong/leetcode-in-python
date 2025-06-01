class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        # pre-process
        # helper function
        # get hamming distance
        def withHammingDistance(word, other):
            res = 0
            L = len(word)
            for x in range(L):
                if word[x] != other[x]:
                    res += 1
                if res > 1:
                    return False
            return True if res == 1 else False

        # process
        from collections import defaultdict
        dicts = defaultdict(list)
        prevs = defaultdict(int)

        for idx, word in enumerate(words):
            L = len(word)
            ml = 1
            prev = -1
            for idx2, l in dicts[L][::-1]:
                if l >= ml:
                    if groups[idx] != groups[idx2]:
                        if withHammingDistance(word, words[idx2]):
                            ml = l + 1
                            prev = idx2
            dicts[L].append((idx, ml))
            prevs[idx] = prev
        print(prevs)

        # post-process
        maxi_idx = -1
        maxi_l = 0
        for l in dicts:
            for idx, ml in dicts[l]:
                if ml > maxi_l:
                    maxi_idx = idx
                    maxi_l = ml

        ans = list()
        idx = maxi_idx
        while idx >= 0:
            ans.append(words[idx])
            idx = prevs[idx]
        ans = ans[::-1]
        return ans


words = ["bab","dab","cab"]
groups = [1,2,2]

words = ["a", "b", "c", "d"]
groups = [1, 2, 3, 4]

words = ["ab", "ac", "ad", "bc", "bd", "cd"]
groups = [1, 1, 2, 3, 2, 3]

words = ["bdb","aaa","ada"]
groups = [2,1,3]

words =["dcaacc","da","ddcbd","dd"]
groups = [2,3,1,4]

solution = Solution()
print(solution.getWordsInLongestSubsequence(words, groups))
