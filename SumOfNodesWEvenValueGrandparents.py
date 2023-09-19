# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sum_ret = 0

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # opt1: traversing a tree (1) depth-first (2) breadth-first using a visited stack/queue
        # opt2: if node is an even grandparent, add to dic -> add all grandchildren after
        self.traverseHelper(root)
        return self.sum_ret
        
    def traverseHelper(self, root):
        if root == None:
            return
        elif root.val%2 == 0:
            if root.left:
                if root.left.left: 
                    self.sum_ret += root.left.left.val
                if root.left.right: 
                    self.sum_ret += root.left.right.val    
            if root.right:
                if root.right.left: 
                    self.sum_ret += root.right.left.val
                if root.right.right: 
                    self.sum_ret += root.right.right.val
        self.traverseHelper(root.left)
        self.traverseHelper(root.right)

    # def traverseHelper(root):
    #     # base case
    #     if root:
    #         nodes = []
    #         return nodes.append(root)
    #     # recursive case
    #     if root.left:
    #         traverseHelper(root.left)
    #     if root.right:
    #         traverseHelper(root.right)
