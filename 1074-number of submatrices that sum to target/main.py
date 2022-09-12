class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])

        def numTarget(array, target):
            prefix = [0] * (N + 1)
            from collections import defaultdict
            dict = defaultdict(int)
            dict[0] = 1

            ans = 0
            for x in range(N):
                prefix[x + 1] = prefix[x] + array[x]
                key = prefix[x + 1] - target
                if key in dict:
                    ans += dict[key]
                dict[prefix[x + 1]] += 1
            return ans

        ans = 0
        for x in range(M):
            total = [0] * N
            for y in range(x, M):
                for z in range(N):
                    total[z] += matrix[y][z]
                ans += numTarget(total, target)
        return ans


matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0

matrix = [[1,-1],[-1,1]]
target = 0

matrix = [[904]]
target = 0

matrix = [[0,1,0,0,1],[0,0,1,1,1],[1,1,1,0,1],[1,1,0,1,1],[0,1,1,0,0]]
target = 1

solution = Solution()
print(solution.numSubmatrixSumTarget(matrix, target))
