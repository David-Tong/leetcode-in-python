class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1 = len(nums1)
        len2 = len(nums2)

        k = (len1 + len2 + 1) // 2
        left = 0
        right = len1

        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1

        c1 = 0
        if m1 > 0:
            if m2 > 0:
                c1 = max(nums1[m1-1], nums2[m2-1])
            else:
                c1 = nums1[m1-1]
        else:
            c1 = nums2[m2-1]

        if (len1 + len2) % 2 != 0:
            return c1
        else:
            c2 = 0
            if m1 < len1:
                if m2 < len2:
                    c2 = min(nums1[m1], nums2[m2])
                else:
                    c2 = nums1[m1]
            else:
                c2 = nums2[m2]
            return (c1 + c2) / 2


nums1 = [1, 3]
nums2 = [2]

#nums1 = [1, 2]
#nums2 = [3, 4]

#nums1 = [-1, 1, 3, 5, 7, 9]
#nums2 = [2, 4, 6, 8, 10, 12, 14, 16]

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
