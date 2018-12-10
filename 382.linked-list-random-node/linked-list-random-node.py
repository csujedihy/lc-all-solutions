# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):

  def __init__(self, head):
    """
    @param head The linked list's head.
    Note that the head is guaranteed to be not null, so it contains at least one node.
    :type head: ListNode
    """
    self.head = head

  def getRandom(self):
    """
    Returns a random node's value.
    :rtype: int
    """
    ans = self.head.val
    head = self.head
    idx = 1
    while head:
      if random.randrange(1, idx + 1) == idx:
        ans = head.val
      head = head.next
      idx += 1
    return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
