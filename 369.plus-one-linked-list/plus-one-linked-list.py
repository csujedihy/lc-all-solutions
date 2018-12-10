# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def plusOne(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def reverse(cur):
      pre = None
      while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      return pre

    p = head = reverse(head)
    carry = 1
    pre = None
    while p:
      val = (p.val + carry) % 10
      carry = 1 if val < p.val else 0
      p.val = val
      pre = p
      p = p.next

    if carry == 1:
      pre.next = ListNode(1)
    return reverse(head)
