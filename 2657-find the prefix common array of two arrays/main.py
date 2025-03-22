class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(A)
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        ans = list()
        common = 0
        for x in range(L):
            dicts[A[x]] += 1
            if dicts[A[x]] == 2:
                common += 1
            dicts[B[x]] += 1
            if dicts[B[x]] == 2:
                common += 1
            ans.append(common)
        return ans


A = [1,3,2,4]
B = [3,1,2,4]

A = [2,3,1]
B = [3,1,2]

solution = Solution()
print(solution.findThePrefixCommonArray(A, B))
