# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    while p.next:
      if p.next.next and p.next.val == p.next.next.val:
        z = p.next
        while z and z.next and z.val == z.next.val:
          z = z.next
        p.next = z.next
      else:
        p = p.next
    return dummy.next
