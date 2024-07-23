class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def getLongestNonDecreasingSS(sequence):
            stack = list()
            for num in sequence:
                if not stack or num >= stack[-1]:
                    stack.append(num)
                else:
                    from bisect import bisect_right
                    idx = bisect_right(stack, num)
                    stack[idx] = num
            return len(sequence) - len(stack)

        L = len(arr)
        ans = 0
        for x in range(k):
            sequence = list()
            for y in range(x, L, k):
                sequence.append(arr[y])
            ans += getLongestNonDecreasingSS(sequence)
        return ans


arr = [5,4,3,2,1]
k = 1

arr = [4,1,5,2,6,2]
k = 2

arr = [4,1,5,2,6,2]
k = 3

arr = [12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
k = 1

solution = Solution()
print(solution.kIncreasing(arr, k))
