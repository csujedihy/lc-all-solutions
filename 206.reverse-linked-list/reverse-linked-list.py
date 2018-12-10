# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseList(self, root):
    if not root or not root.next:
      return root

    ret = self.reverseList(root.next)
    root.next.next = root
    root.next = None
    return ret

  def _reverseList(self, head):
    pre = None
    cur = head
    while cur:
      tmp = cur.next
      cur.next = pre
      pre = cur
      cur = tmp
    return pre

  # iteratively as queue head inserting
  def __reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dHead = dummy = ListNode(-1)
    p = head
    while p:
      tmp = dummy.next
      dummy.next = p
      p = p.next
      dummy.next.next = tmp
    return dHead.next

  # easily leads to a circle. Remove current node's next after recursive call.
  def ___reverseList(self, head):
    self.newHead = None

    def rec(head):
      if not head:
        return head
      p = rec(head.next)
      head.next = None
      if p:
        p.next = head
      else:
        self.newHead = head
      return head

    rec(head)
    return self.newHead
