class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # pre-process
        S = len(s)
        L = len(indices)

        # process
        # helper function
        def replace(idx):
            l = len(sources[idx])
            s_idx = indices[idx]
            if s[s_idx: s_idx + l] == sources[idx]:
                return s_idx, s_idx + l, targets[idx]
            else:
                return None

        replacements = list()
        for idx in range(L):
            replacement = replace(idx)
            if replacement:
                replacements.append(replacement)
        replacements = sorted(replacements)
        # print(replacements)

        idx = 0
        keeps = list()
        for replacement in replacements:
            start, end, _ = replacement
            if start > idx:
                keeps.append((idx, start, s[idx: start]))
            idx = end
        if idx != S:
            keeps.append((idx, S, s[idx: S]))

        # print(replacements)
        # print(keeps)

        tokens = replacements
        tokens.extend(keeps)
        tokens = sorted(tokens)
        print(tokens)

        ans = ""
        for token in tokens:
            ans += token[2]
        return ans


s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

s = "abcd"
indices = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]

s = "abcd"
indices = [2, 0]
sources = ["ab","ec"]
targets = ["eee","ffff"]

s = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg","ggq","mo"]
targets = ["s","so","bfr"]

solution = Solution()
print(solution.findReplaceString(s, indices, sources, targets))
