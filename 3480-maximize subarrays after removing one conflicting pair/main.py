class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        # pre-process
        min1, min2 = [float("inf")] * (n + 1), [float("inf")] * (n + 1)
        for conflictingPair in conflictingPairs:
            a, b = (min(conflictingPair[0], conflictingPair[1]),
                    max(conflictingPair[0], conflictingPair[1]))
            if min1[a] > b:
                min2[a] = min1[a]
                min1[a] = b
            elif min2[a] > b:
                min2[a] = b

        print(min1)
        print(min2)

        # process
        ans = 0
        ib1 = n
        b2 = float("inf")
        del_count = [0] * (n + 1)
        for x in range(n, 0, -1):
            if min1[ib1] > min1[x]:
                b2 = min(b2, min1[ib1])
                ib1 = x
            else:
                b2 = min(b2, min1[x])
            ans += min(min1[ib1], n + 1) - x
            del_count[ib1] += min(min(b2, min2[ib1]), n + 1) - min(min1[ib1], n + 1)
        print(del_count)
        return ans + max(del_count)


n = 4
conflictingPairs = [[2,3],[1,4]]

n = 4
conflictingPairs = [[2,3],[1,4],[1,3],[1,2]]

# n = 5
# conflictingPairs = [[1,2],[2,5],[3,5]]

solution = Solution()
print(solution.maxSubarrays(n, conflictingPairs))
