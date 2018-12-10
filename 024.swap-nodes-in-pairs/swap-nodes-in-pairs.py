# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def reverseList(head, k):
      pre = None
      cur = head
      while cur and k > 0:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        k -= 1
      head.next = cur
      return cur, pre

    if not head or not head.next:
      return head
    ret = head.next
    p = head
    pre = None
    while p:
      next, newHead = reverseList(p, 2)
      if pre:
        pre.next = newHead
      pre = p
      p = next
    return ret
