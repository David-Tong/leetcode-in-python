class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if len(arr) < 3:
            return 0

        slow = 0
        res = 0
        while True:
            while slow < len(arr) - 1 and arr[slow] == arr[slow + 1]:
                slow += 1

            if slow == len(arr) - 1:
                break

            fast = slow + 1
            up = False
            down = False

            while fast < len(arr) and arr[fast - 1] < arr[fast]:
                fast += 1
                up = True

            while fast < len(arr) and arr[fast - 1] > arr[fast]:
                fast += 1
                down = True

            fast -= 1
            if up and down:
                res = max(res, fast - slow + 1)

            slow = fast

        return res


arr = [2, 1, 4, 7, 3, 2, 5]
arr = [1, 2, 2, 2, 2]

solution = Solution()
print(solution.longestMountain(arr))
