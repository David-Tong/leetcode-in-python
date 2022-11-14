class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L = len(s)
        A = 26
        # cache - cache[i][a][l][k] - cache dfs result for dft(i, a, l, k)
        self.cache = [[[[-1] * (k + 1) for _ in range(L + 1)] for _ in range(A + 1)] for _ in range(L + 1)]

        # dfs - return the min length for a string
        #       for to search part started with s[i:] and k character left to delete
        #       for searched part ended with character a and with the length of l
        def dfs(i, a, l, k):
            # convert to idx
            idx = 26
            if len(a) == 1:
                idx = ord(a) - ord('a')
            # invalid case
            if k < 0:
                return float("inf")
            # delete all
            if i + k >= L:
                return 0
            # return searched result
            if self.cache[i][idx][l][k] != -1:
                return self.cache[i][idx][l][k]
            # the s[i] == end character of searched part, concat them
            # don't delete
            if s[i] == a:
                carry = 0
                if l == 1 or l == 9 or l == 99:
                    carry = 1
                self.cache[i][idx][l][k] = carry + dfs(i + 1, a, l + 1, k)
            else:
                # get min of delete or keep
                self.cache[i][idx][l][k] = min(1 + dfs(i + 1, s[i], 1, k), dfs(i + 1, a, l, k - 1))
            return self.cache[i][idx][l][k]

        return dfs(0, '', 0, k)


s = "aaabcccd"
k = 2

s = "aabbaa"
k = 2

s = "aaaaaaaaaaa"
k = 0

s = "aabaabbcbbbaccc"
k = 6

s = "dceabdabccbaecdabdccbadcacbbacbdabdeacdaeddccbbdcdbacbc"
k = 35

solution = Solution()
print(solution.getLengthOfOptimalCompression(s, k))
