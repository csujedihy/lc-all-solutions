# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    def reverseList(root):
      pre = None
      cur = root
      while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
      return pre

    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    newHead = reverseList(slow)
    p1 = head
    p2 = newHead
    while p1 and p2:
      if p1.val != p2.val:
        return False
      p1 = p1.next
      p2 = p2.next
    return True
