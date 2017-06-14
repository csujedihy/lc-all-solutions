# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(-1)
        carry = 0
        while l1 or l2:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
                
            c = carry
            carry = 0
            sum = a + b + c
            if sum >= 10:
                carry = 1
                head.next = ListNode(sum - 10)
            else:
                head.next = ListNode(sum)
            head = head.next

        if carry == 1:
            head.next = ListNode(1)
        
            
        return dummy.next
            
            
            
                