# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = {}
        curr = head
        temp_node = None
        if (curr == None or curr.next == None):
            return False
        pos = 0
        while curr.next != None:
            # if node is in seen dict, there is a cycle
            if curr in seen:
                # check that the next node is in the cycle
                # if seen[curr.next] == ...
                return True
            seen[curr] = pos
            curr = curr.next
            pos += 1
        return False
