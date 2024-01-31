S# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        ## ATTEMPT 2    
        # traverse through root to find matching subroot
        if subRoot == None:
            return True

        if (root == None):
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # currNode = ''
        # i = 0
        # root_stack = [root]
        # sub_stack = [subRoot]
        # match = False

        # while i < len(stack):
        #     currNode = stack[i]
        #     if currNode == subRoot:
                
    # recursive helper function that determines wether or not two trees are the same 
    def sameTree(self, node1, node2):
        if (node1 == None) and (node2 == None):
            return True

        if (node1 and node2) and (node1.val == node2.val):
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)

        return False

        ## ATTEMPT 1 - implemented solution with input type of arr instead of TreeNode
        # # iterate in parallel to find matching subRoot

        # n_root = len(root)
        # n_sroot = len(subRoot)
        
        # i_root, i_sroot = n_root, n_sroot
        # for j in range(n_root-1, -1, -1):
        #     if root[j] == subRoot[n_sroot]:
        #         i_sroot = n_sroot
        #         i_root = j
        #         while (i_root >= 0):
        #             if root[i_root] == subRoot[i_sroot]:
        #                 i_root -= 1
        #                 i_sroot -= 1
        #                 if i_sroot <= -1:
        #                     return True
        #             else:
        #                 break
        # return False
            
                        
        
