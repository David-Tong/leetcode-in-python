class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        # pre-process
        L = len(words)

        idxes = list()
        idx = 0
        while idx < L:
            if words[idx] == target:
                idxes.append(idx)
            idx += 1

        def distance(idx, idx2):
            return (idx - idx2 + L) % L

        # process
        if len(idxes) == 0:
            return -1

        ans = float('inf')
        for idx in idxes:
            ans = min(ans, min(distance(startIndex, idx), distance(idx, startIndex)))
        return ans


words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1

words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0

words = ["i","eat","leetcode"]
target = "ate"
startIndex = 0

words = ["ibkgecmeyx","jsdkekkjsb","gdjgdtjtrs","jsdkekkjsb","jsdkekkjsb","jsdkekkjsb","gdjgdtjtrs","msjlfpawbx","pbgjhutcwb","gdjgdtjtrs"]
target = "pbgjhutcwb"
startIndex = 0

words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8

solution = Solution()
print(solution.closestTarget(words, target, startIndex))
