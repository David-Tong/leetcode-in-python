class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # pre-process
        L = len(s)
        idxes = list()
        for idx, ch in enumerate(s):
            if ch == c:
                idxes.append(idx)
        idxes = [float("-inf")] + idxes + [float("inf")]
        # print(idxes)

        # process
        idx = 0
        left, right = idxes[idx], idxes[idx + 1]
        ans = list()
        for x in range(L):
            ans.append(min(x - left, right - x))
            if x == right:
                idx += 1
                left, right = idxes[idx], idxes[idx + 1]
        return ans


s = "loveleetcode"
c = "e"

s = "aaab"
c = "b"

solution = Solution()
print(solution.shortestToChar(s, c))
