class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def doConstruct(nums):
            if len(nums) == 0:
                return None

            maxi = max(nums)
            for idx, num in enumerate(nums):
                if maxi == num:
                    break

            node = TreeNode(maxi)
            node.left = doConstruct(nums[:idx])
            node.right = doConstruct(nums[idx + 1:])

            return node

        return doConstruct(nums)


nums = [3,2,1,6,0,5]
nums = [3,2,1]

solution = Solution()
node = solution.constructMaximumBinaryTree(nums)

print(node.val)
