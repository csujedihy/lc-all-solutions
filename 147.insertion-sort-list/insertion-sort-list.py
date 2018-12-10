class Solution(object):
  def insertionSortList(self, head):
    p = dummy = ListNode(0)
    cur = dummy.next = head
    while cur and cur.next:
      val = cur.next.val
      if cur.val < val:
        cur = cur.next
        continue
      if p.next.val > val:
        p = dummy
      while p.next.val < val:
        p = p.next
      new = cur.next
      cur.next = new.next
      new.next = p.next
      p.next = new
    return dummy.next
