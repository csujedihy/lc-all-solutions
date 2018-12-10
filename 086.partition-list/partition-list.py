# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if head is None:
      return None
    dummy = ListNode(-1)
    dummy.next = head
    sHead = sDummy = ListNode(-1)
    p = dummy
    while p and p.next:
      if p.next.val < x:
        sDummy.next = p.next
        p.next = p.next.next
        sDummy = sDummy.next
      else:
        p = p.next
      # if you change p.next then make sure you wouldn't change p in next run
    sDummy.next = dummy.next
    return sHead.next
