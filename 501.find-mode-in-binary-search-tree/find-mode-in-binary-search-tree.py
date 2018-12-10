# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def findMode(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def visit(v):
      if v != self.pre:
        self.pre = v
        self.cnt = 0
      self.cnt += 1
      if self.cnt > self.maxFreq:
        self.maxFreq = self.cnt
        self.modeCnt = 1
      elif self.cnt == self.maxFreq:
        if self.ans:
          self.ans[self.modeCnt] = v
        self.modeCnt += 1

    def inorder(root):
      if root:
        inorder(root.left)
        visit(root.val)
        inorder(root.right)

    self.pre = None
    self.ans = None
    self.maxFreq = self.modeCnt = self.cnt = 0
    inorder(root)
    self.ans = [0] * self.modeCnt
    self.modeCnt = self.cnt = 0
    inorder(root)
    return self.ans
