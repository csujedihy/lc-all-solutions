class Solution:
  def __init__(self):
    self.n1 = None
    self.n2 = None
    self.pre = None

  def findBadNode(self, root):
    if root is None: return
    self.findBadNode(root.left)
    if self.pre is not None:
      if root.val < self.pre.val:
        if self.n1 is None:
          self.n1 = self.pre
          self.n2 = root
        else:
          self.n2 = root
    self.pre = root
    self.findBadNode(root.right)

  def recoverTree(self, root):
    self.findBadNode(root)
    if self.n1 is not None and self.n2 is not None:
      self.n1.val, self.n2.val = self.n2.val, self.n1.val
