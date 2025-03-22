class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict

        dicts = defaultdict(dict)
        for s in strs:
            if s not in dicts[len(s)]:
                dicts[len(s)][s] = 0
            dicts[len(s)][s] += 1

        # process
        # helper
        # is str1 a subsequence of str2?
        def isSubsequence(str1, str2):
            L, L2 = len(str1), len(str2)
            if L >= L2:
                return False
            else:
                idx, idx2 = 0, 0
                while idx < L and idx2 < L2:
                    if str1[idx] == str2[idx2]:
                        idx += 1
                    idx2 += 1
                return True if idx == L else False

        for l in sorted(dicts.keys(), reverse=True):
            for s in dicts[l]:
                if dicts[l][s] == 1:
                    contain = False
                    for st in strs:
                        if isSubsequence(s, st):
                            contain = True
                    if not contain:
                        return l
        return -1


strs = ["aba","cdc","eae"]
strs = ["aaa","aaa","aa"]
strs = ["aabbcc", "aabbcc","cb","abc"]

solution = Solution()
print(solution.findLUSlength(strs))
