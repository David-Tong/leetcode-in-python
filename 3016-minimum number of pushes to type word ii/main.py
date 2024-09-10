class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for c in word:
            dicts[c] += 1
        pairs = [(key, dicts[key]) for key in dicts]
        pairs = sorted(pairs, key=lambda x: -1 * x[1])

        maps = defaultdict(int)
        for idx, pair in enumerate(pairs):
            key = pair[0]
            maps[key] = idx // 8 + 1

        # process
        ans = 0
        for c in word:
            ans += maps[c]
        return ans


word = "abcdde"
word = "aabbccddeeffgghhiiiiii"
word = "aasjuqwgfuqwhiqwiqwjishdudqiwdhuqwdiawuefewnfmwefmewfijaaaaslsdfmiewfnievnoewjwedasaabbb"

solution = Solution()
print(solution.minimumPushes(word))
