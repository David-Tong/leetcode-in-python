class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        # pre-process
        L = len(target)
        processed = ""
        idx = 0
        while idx < L:
            if idx > 0:
                if target[idx] == target[idx - 1]:
                    idx += 1
                    continue
            processed += target[idx]
            idx += 1
        print(processed)

        # process
        if processed[0] == "0":
            ans = len(processed) - 1
        else:
            ans = len(processed)
        return ans


target = "10111"
target = "101"
target = "00000"
target = "010111"
target = "01010111"

solution = Solution()
print(solution.minFlips(target))
