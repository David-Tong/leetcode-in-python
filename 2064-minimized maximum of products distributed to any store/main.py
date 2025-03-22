class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def canDistribute(target):
            idx, count = 0, 0
            quantity = quantities[idx]
            while count < n and idx < L:
                if quantity <= target:
                    idx += 1
                    if idx < L:
                        quantity = quantities[idx]
                else:
                    quantity -= target
                count += 1
            if count == n:
                if idx == L:
                    return True
            elif count < n:
                return True
            return False
        
        # pre-process
        L = len(quantities)
        quantities = sorted(quantities)

        # process
        left, right = 1, 10 ** 5
        while left + 1 < right:
            middle = (left + right) // 2
            if canDistribute(middle):
                right = middle
            else:
                left = middle + 1

        if canDistribute(left):
            return left
        else:
            return right


n = 6
quantities = [11,6]

n = 7
quantities = [15,10,10]

n = 1
quantities = [100000]

solution = Solution()
print(solution.minimizedMaximum(n, quantities))
