class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L = len(s)
        # cache - cache[i][k] the min length for compression of s[i:] with at most k deletion
        self.cache = [[-1] * (k + 1) for _ in range(L)]

        # dfs - return the min length for compression of s[i:] with at most k deletion
        def dfs(i, k):
            # invalid case
            if k < 0:
                return float("inf")
            # delete all
            if i + k >= L:
                return 0
            # return searched result
            if self.cache[i][k] != -1:
                return self.cache[i][k]

            # delete case
            ans = dfs(i + 1, k - 1)

            # loop every position j in s[i:], to merge and delete
            length = 0
            same = 0
            different = 0

            j = i
            while j < L and different <= k:
                if s[i] == s[j]:
                    same += 1
                    if same <= 2 or same == 10 or same == 100:
                        length += 1
                else:
                    different += 1
                ans = min(ans, length + dfs(j + 1, k - different))
                j += 1
            self.cache[i][k] = ans
            return ans

        return dfs(0, k)


s = "aabbaa"
k = 2

s = "dceabdabccbaecdabdccbadcacbbacbdabdeacdaeddccbbdcdbacbc"
k = 35

solution = Solution()
print(solution.getLengthOfOptimalCompression(s, k))
