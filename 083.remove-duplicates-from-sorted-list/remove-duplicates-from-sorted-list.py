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
    dummy = ListNode(None)
    dummy.next = head
    p = dummy

    while p and p.next:
      if p.val == p.next.val:
        p.next = p.next.next
      else:
        p = p.next
    return dummy.next
