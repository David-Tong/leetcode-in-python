class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildBST(nums, left, right):
            if left < right:
                middle = (left + right) // 2
                root = TreeNode(nums[middle])
                root.left = buildBST(nums, left, middle - 1)
                root.right = buildBST(nums, middle + 1, right)
                return root
            elif left == right:
                return TreeNode(nums[left])

        return buildBST(nums, 0, len(nums) - 1)
