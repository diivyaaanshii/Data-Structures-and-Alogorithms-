# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        leftDepth=self.minDepth(root.left)
        rightDepth=self.minDepth(root.right)
        if not root.left or not root.right:
            return 1+leftDepth+rightDepth
        return 1+ min(leftDepth,rightDepth)