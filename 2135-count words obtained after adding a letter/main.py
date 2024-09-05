class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        startDicts = defaultdict(bool)
        for startWord in startWords:
            key = "".join(sorted(list(startWord)))
            startDicts[key] = 1
        targetDicts = defaultdict(bool)
        for targetWord in targetWords:
            key = "".join(sorted(list(targetWord)))
            targetDicts[key] += 1

        # process
        ans = 0
        for key in targetDicts:
            for x in range(len(key)):
                start = key[:x] + key[x + 1:]
                if start in startDicts:
                    ans += targetDicts[key]
                    break
        return ans


startWords = ["ant","act","tack"]
targetWords = ["tack","act","acti"]

startWords = ["ab","a"]
targetWords = ["abc","abcd"]

startWords = ["ab"]
targetWords = ["acb", "adb", "azb"]

startWords = ["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"]
targetWords = ["r","am","jg","umhjo","fov","lujy","b","uz","y"]

solution = Solution()
print(solution.wordCount(startWords, targetWords))
