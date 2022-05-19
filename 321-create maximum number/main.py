class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def makeMaxNumber(nums, k):
            stack = []
            to_pop = len(nums) - k
            for num in nums:
                while stack and stack[-1] < num and to_pop > 0:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)
            return stack[:k]

        def mergeMaxNumbers(nums1, nums2):
            idx1 = 0
            idx2 = 0
            ans = []
            while idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1:] >= nums2[idx2:]:
                    ans.append(nums1[idx1])
                    idx1 += 1
                else:
                    ans.append(nums2[idx2])
                    idx2 += 1

            while idx1 < len(nums1):
                ans.append(nums1[idx1])
                idx1 += 1

            while idx2 < len(nums2):
                ans.append(nums2[idx2])
                idx2 += 1

            return ans

        # enumerate select x from nums1 and select k - x from nums2, get the maximum number
        ans = [0]
        for x in range(k + 1):
            y = k - x
            if x <= len(nums1) and y <= len(nums2):
                max1 = makeMaxNumber(nums1, x)
                max2 = makeMaxNumber(nums2, y)
                if x == 0:
                    ans = max(ans, max2)
                elif y == 0:
                    ans = max(ans, max1)
                else:
                    ans = max(ans, mergeMaxNumbers(max1, max2))
        return ans


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5

nums1 = [6,7]
nums2 = [6,0,4]
k = 5

nums1 = [3,9]
nums2 = [8,9]
k = 3

nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 15

nums1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
nums2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
k = 100

nums1 = [8,1,8,8,6]
nums2 = [4]
k = 2

solution = Solution()
print(solution.maxNumber(nums1, nums2, k))
