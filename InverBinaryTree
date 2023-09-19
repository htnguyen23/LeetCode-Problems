# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tempNode = None
        # rec case: if root has L or R children
        # L rec
        if not root:
            return root
        if (root.left != None):
            self.invertTree(root.left)
        # R rec
        if (root.right != None):
            self.invertTree(root.right)
        # base case: if root has no children
        tempNode = root.left
        root.left = root.right
        root.right = tempNode
        return root
        

        
