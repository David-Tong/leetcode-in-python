class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(code)
        if k > 0:
            left = 1
            right = k
            total = sum(code[left:right + 1])
        elif k < 0:
            left = k
            right = -1
            total = sum(code[left:])
        else:
            return [0] * L

        # process
        ans = list()
        for x in range(L):
            ans.append(total)
            total -= code[left]
            left = (left + 1) % L
            right = (right + 1) % L
            total += code[right]
        return ans


code = [5,7,1,4]
k = 3

code = [1,2,3,4]
k = 0

code = [2,4,9,3]
k = -2

solution = Solution()
print(solution.decrypt(code, k))
