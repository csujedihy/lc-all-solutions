# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    def reverse(root):
      pre = None
      cur = root
      while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
      return pre

    if not head or not head.next:
      return
    slow = fast = head
    pre = None
    while fast and fast.next:
      pre = slow
      slow = slow.next
      fast = fast.next.next
    if pre:
      pre.next = None
    newHead = reverse(slow)
    ret = dummy = ListNode(-1)
    p1 = head
    p2 = newHead
    while p1 and p2:
      dummy.next = p1
      p1 = p1.next
      dummy = dummy.next
      dummy.next = p2
      p2 = p2.next
      dummy = dummy.next

    if p2:
      dummy.next = p2
    head.next = ret.next.next
