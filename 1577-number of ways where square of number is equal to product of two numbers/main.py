class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts1 = defaultdict(int)
        dicts2 = defaultdict(int)
        for num1 in nums1:
            dicts1[num1] += 1
        for num2 in nums2:
            dicts2[num2] += 1

        # process
        ans = 0

        # type 1
        for num1 in nums1:
            for num2 in set(nums2):
                num = num1 * num1 * 1.0 / num2
                if abs(num - int(num)) < 10e-9:
                    if num in nums2:
                        if num == num2:
                            if dicts2[num2] > 1:
                                ans += dicts2[num2] * (dicts2[num2] - 1)
                        else:
                            ans += dicts2[num2] * dicts2[num]

        # type 2
        for num2 in nums2:
            for num1 in set(nums1):
                num = num2 * num2 * 1.0 / num1
                if abs(num - int(num)) < 10e9:
                    if num in nums1:
                        if num == num1:
                            if dicts1[num1] > 1:
                                ans += dicts1[num1] * (dicts1[num1] - 1)
                        else:
                            ans += dicts1[num1] * dicts1[num]
        ans = ans // 2
        return ans


nums1 = [7,4]
nums2 = [5,2,8,9]

nums1 = [1,1]
nums2 = [1,1,1]

nums1 = [7,7,8,3]
nums2 = [1,2,9,7]

nums1 = [2,4,6]
nums2 = [1,2,2,2,2,4,8,16,36]

solution = Solution()
print(solution.numTriplets(nums1, nums2))
