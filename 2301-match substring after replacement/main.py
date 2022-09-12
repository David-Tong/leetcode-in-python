class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        def isMatch(ch, target, dicts):
            if ch == target:
                return True
            else:
                if target in dicts[ch]:
                    return True
                else:
                    return False

        from collections import defaultdict
        dicts = defaultdict(list)
        for key, val in mappings:
            dicts[val].append(key)

        M = len(s)
        N = len(sub)

        idx = 0
        while idx <= M - N:
            offset = 0
            while offset < N:
                ch = s[idx + offset]
                target = sub[offset]
                if isMatch(ch, target, dicts):
                    offset += 1
                else:
                    offset = 0
                    break
            if offset == N:
                return True
            idx += 1
        return False


s = "fool3e7bar"
sub = "leet"
mappings = [["e","3"],["t","7"],["t","8"]]

s = "fooleetbar"
sub = "f00l"
mappings = [["o", "0"]]

s = "Fool33tbaR"
sub = "leetd"
mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]

s = "gfos3tks9q9f1w30t38ga9vbwlm"
sub = "juzq2kcvo22pgo81c0"
mappings = [["3","e"],["b","8"],["e","3"],["0","o"],["8","b"],["s","5"],["l","1"],["o","0"]]

s = "eeeegeeeegeeeegeeeegeeeegeeeegeeeeg"
sub = "eeeee"
mappings = [["e","a"],["e","b"],["e","c"],["e","d"],["e","f"],["e","h"],["e","i"],["e","j"],["e","k"],["e","l"],["e","m"],["e","n"],["e","o"],["e","p"],["e","q"],["e","r"],["e","s"],["e","t"],["e","u"],["e","v"],["e","w"],["e","x"],["e","y"],["e","z"],["e","0"],["e","1"],["e","2"],["e","3"],["e","4"],["e","5"],["e","6"],["e","7"],["e","8"],["e","9"],["g","a"],["g","b"],["g","c"],["g","d"],["g","f"],["g","h"],["g","i"],["g","j"],["g","k"],["g","l"],["g","m"],["g","n"],["g","o"],["g","p"],["g","q"],["g","r"],["g","s"],["g","t"],["g","u"],["g","v"],["g","w"],["g","x"],["g","y"],["g","z"],["g","0"],["g","1"],["g","2"],["g","3"],["g","4"],["g","5"],["g","6"],["g","7"],["g","8"],["g","9"]]

solution = Solution()
print(solution.matchReplacement(s, sub, mappings))
