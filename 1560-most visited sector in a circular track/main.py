class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(rounds)
        visited = [0] * n

        # process
        idx = 0
        visited[rounds[idx] - 1] = 1
        while idx < L - 1:
            idx2 = rounds[idx] - 1
            count = (rounds[idx + 1] - rounds[idx] + n) % n
            while count:
                count -= 1
                idx2 += 1
                if idx2 >= n:
                    idx2 %= n
                visited[idx2] += 1
            idx += 1
            # print(visited)
        # print(visited)

        ans = list()
        maxi = max(visited)
        idx = 0
        while idx < n:
            if visited[idx] == maxi:
                ans.append(idx + 1)
            idx += 1
        return ans


n = 4
rounds = [1,3,1,2]

n = 2
rounds = [2,1,2,1,2,1,2,1,2]

n = 7
rounds = [1,3,5,7]

n = 10
rounds = [3,5,1,3,7]

"""
import random
n = 100
rounds = [random.randint(1,10) for _ in range(5)]
print(rounds)
"""

solution = Solution()
print(solution.mostVisited(n, rounds))
