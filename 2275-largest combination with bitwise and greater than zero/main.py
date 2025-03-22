class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        # pre-process
        L = 24
        bits = [0] * L
        for candidate in candidates:
            for x in range(L):
                if candidate >> x & 1:
                    bits[x] += 1
        print(bits)

        # process
        ans = max(bits)
        return ans


candidates = [16,17,71,62,12,24,14]
candidates = [8,8]
candidates = [_ for _ in range(1000)]

solution = Solution()
print(solution.largestCombination(candidates))
