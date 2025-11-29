class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        # helper function
        def total(code):
            # print(code)
            res = 0
            for idx, c in enumerate(code):
                # print(idx, c)
                res += mat[idx][c]
            return res

        def mutate(code):
            mutations = list()
            for idx, c in enumerate(code):
                if code[idx] < N - 1:
                    mutation = code[:idx] + [code[idx] + 1] + code[idx + 1:]
                    mutations.append(mutation)
            return mutations

        def hash(code):
            return "-".join([str(_) for _ in code])

        # code = [0, 1, 0]
        # print(mutate(code))

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        visited = set()

        code = [0] * M
        heappush(heap, (total(code), code))
        visited.add(hash(code))

        idx = 0
        while idx < k:

            ans, code = heappop(heap)
            mutations = mutate(code)
            for mutation in mutations:
                if hash(mutation) not in visited:
                    heappush(heap, (total(mutation), mutation))
                    visited.add(hash(mutation))
            idx += 1
        return ans


mat = [[1,3,11],[2,4,6]]
k = 5

mat = [[1,3,11],[2,4,6]]
k = 9

mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7

solution = Solution()
print(solution.kthSmallest(mat, k))
