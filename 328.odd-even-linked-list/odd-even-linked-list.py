# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    o = odd = ListNode(-1)
    e = even = ListNode(-1)
    p = head
    isOdd = True
    while p:
      if isOdd:
        o.next = p
        o = o.next
        isOdd = False
      else:
        e.next = p
        isOdd = True
        e = e.next
      p = p.next
    e.next = None
    o.next = even.next
    return odd.next
