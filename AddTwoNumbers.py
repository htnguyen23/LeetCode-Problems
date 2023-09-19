# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # get number from nodes in reverse
        l1_str = ""
        l2_str = ""

        curr_node = l1
        while (curr_node != None) :
            #print(curr_node)
            l1_str = str(curr_node.val) + l1_str 
            curr_node = curr_node.next
        curr_node = l2
        while (curr_node != None) :
            #print(curr_node)
            l2_str = str(curr_node.val) + l2_str 
            curr_node = curr_node.next

        # find sum
        l1_num = int(l1_str)
        l2_num = int(l2_str)
        sum_str = str(l1_num + l2_num)
        print(sum_str)

        # return sum in reverse nodes
        lsum = ListNode(int(sum_str[-1]))
        curr_node = lsum
        #print(type(curr_node))
        for i in reversed(range(0, len(sum_str)-1)):
            print(i)
            #lsum = ListNode(int(sum_str[i]))
            #lsum = lsum.next
            curr_node.next = ListNode(int(sum_str[i])) #next = None
            curr_node = curr_node.next 
            #print(sum_str[i])
        return lsum
