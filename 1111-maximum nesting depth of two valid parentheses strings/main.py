class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # pre-process
        L = len(seq)

        maxi = 0
        depth = 0
        idx = 0
        while idx < L:
            if seq[idx] == '(':
                depth += 1
                maxi = max(maxi, depth)
            elif seq[idx] == ')':
                depth -= 1
            idx += 1
        target = (maxi + 1) // 2
        # print(maxi)
        # print(target)

        # process
        ans = list()
        depth = 0
        idx = 0
        while idx < L:
            if seq[idx] == '(':
                depth += 1
                if depth > target:
                    ans.append(1)
                else:
                    ans.append(0)
            elif seq[idx] == ')':
                if depth > target:
                    ans.append(1)
                else:
                    ans.append(0)
                depth -= 1
            idx += 1
        return ans


seq = "(()())"
seq = "()(())()"
seq = "(((())))((()))()(((())))"

solution = Solution()
print(solution.maxDepthAfterSplit(seq))
