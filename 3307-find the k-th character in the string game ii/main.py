class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        # pre-process
        # helper functions
        # get operation
        def getOperation(k):
            res = 0
            while k:
                k >>= 1
                res += 1
            return res - 1

        # remove the leading one
        def reduce(k):
            if len(bin(k)) > 3:
                return int(bin(k)[3:],2)
            else:
                return 0

        # get new ch after changing
        def change(ch):
            return chr(ord('a') + (ord(ch) - ord('a') + 1) % 26)

        # process
        # recursion
        def getCharacter(k):
            if k == 0:
                return 'a'
            else:
                operation = operations[getOperation(k)]
                ch = getCharacter(reduce(k))
                if operation == 0:
                    return ch
                elif operation == 1:
                    return change(ch)

        ans = getCharacter(k - 1)
        return ans


k = 5
operations = [0,0,0]

k = 10
operations = [0,1,0,1]

k = 15
operations = [0,1,0,1]

import random
k = 10 ** 14
operations = list()
for x in range(100):
    operations.append(random.randint(0, 1))
print(k)
print(operations)

k = 1
operations = [1]

solution = Solution()
print(solution.kthCharacter(k, operations))
