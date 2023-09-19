# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_count = 1
        curr_node = head
        # head_return = ListNode(curr_node.val)
        list_len = 0
        while (not (curr_node.next == None)) :
            list_len += 1;

        curr_node = head
        for i in range(1, list_len):
            if (node_count == (list_len-n)):
                next_node = curr_node.next 
                if (not (next_node == None)):
                    curr_node.next = next_node.next
                else:
                    curr_node.next = None
            curr_node = curr_node.next
            node_count += 1   

        return head
             