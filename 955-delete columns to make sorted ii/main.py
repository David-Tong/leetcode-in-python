class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # pre-process
        M = len(strs)
        N = len(strs[0])
        deletions = [False] * N

        # process
        def delete(col, start, end):
            if 0 <= col < N and 0 <= start < M and 0 <= end < M and start < end:
                if deletions[col]:
                    delete(col + 1, start, end)
                else:
                    row = start
                    next_start = -1
                    while row < end:
                        if strs[row][col] == strs[row + 1][col]:
                            if next_start == -1:
                                next_start = row
                        else:
                            if next_start != -1:
                                next_end = row
                                delete(col + 1, next_start, next_end)
                                next_start = -1

                            if strs[row][col] > strs[row + 1][col]:
                                deletions[col] = True
                                break
                        row += 1

                    if next_start != -1:
                        next_end = end
                        delete(col + 1, next_start, next_end)

        prev = sum(deletions)
        curr = -1
        while True:
            delete(0, 0, M - 1)
            # print(deletions)
            curr = sum(deletions)
            if curr != prev:
                prev = curr
            else:
                break

        # post-process
        ans = sum(deletions)
        return ans


strs = ["ca","bb","ac"]
strs = ["xc","yb","za"]
strs = ["zyx","wvu","tsr"]
strs = ["abc","bbc","bac","bad","baa"]
strs = ["abcd","accd", "abcc", "bbac"]
strs = ["vdy","vei","zvc","zld"]
strs = ["jqonkbi","joeikeh","lqolzdm"]

solution = Solution()
print(solution.minDeletionSize(strs))
