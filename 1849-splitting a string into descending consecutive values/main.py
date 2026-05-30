class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # pre-process
        L = len(s)

        # process
        # dfs
        def split(prev, pivot, parts):
            # print(prev, pivot, parts)
            if pivot == L:
                return True if parts > 1 else False

            idx = pivot
            while idx < L:
                val = int(s[pivot:idx + 1])
                if prev == -1:
                    if split(val, idx + 1, parts + 1):
                        return True
                else:
                    if val == prev - 1:
                        if split(prev - 1, idx + 1, parts + 1):
                            return True
                idx += 1
            return False

        return split(-1, 0, 0)


s = "1234"
s = "050043"
s = "9080701"
s = "001"
s = "200100"

solution = Solution()
print(solution.splitString(s))
