# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
  # @param root, a tree link node
  # @return nothing
  def connect(self, root):
    p = root
    pre = None
    head = None
    while p:
      if p.left:
        if pre:
          pre.next = p.left
        pre = p.left
      if p.right:
        if pre:
          pre.next = p.right
        pre = p.right
      if not head:
        head = p.left or p.right
      if p.next:
        p = p.next
      else:
        p = head
        head = None
        pre = None
