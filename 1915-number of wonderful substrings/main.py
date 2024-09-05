class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        def encode(dicts):
            code = ""
            for x in range(10):
                key = chr(ord('a') + x)
                if dicts[key] % 2 == 0:
                    code += "0"
                else:
                    code += "1"
            return code

        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        codes = defaultdict(int)

        ans = 0
        codes["0" * 10] = 1
        for ch in word:
            dicts[ch] += 1
            code = encode(dicts)

            if code in codes:
                ans += codes[code]

            for x in range(10):
                if code[x] == "1":
                    reversed = code[:x] + "0" + code[x + 1:]
                else:
                    reversed = code[:x] + "1" + code[x + 1:]
                if reversed in codes:
                    ans += codes[reversed]
            codes[code] += 1
        return ans


word = "aba"
word = "aabb"
word = "he"
word = "abbabababababababaaabbbaa"
word = "aaaaaaaaaaaaaaaaaaaaaaaaaa"

solution = Solution()
print(solution.wonderfulSubstrings(word))
