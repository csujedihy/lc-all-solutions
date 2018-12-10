# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    fast = slow = dummy

    while n and fast:
      fast = fast.next
      n -= 1

    while fast.next and slow.next:
      fast = fast.next
      slow = slow.next

    slow.next = slow.next.next
    return dummy.next
