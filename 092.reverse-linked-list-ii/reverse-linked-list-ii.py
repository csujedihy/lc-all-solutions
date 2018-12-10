# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    def reverse(root, prep, k):
      cur = root
      pre = None
      next = None
      while cur and k > 0:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        k -= 1
      root.next = next
      prep.next = pre
      return pre

    dummy = ListNode(-1)
    dummy.next = head
    k = 1
    p = dummy
    start = None
    while p:
      if k == m:
        start = p
      if k == n + 1:
        reverse(start.next, start, n - m + 1)
        return dummy.next
      k += 1
      p = p.next
