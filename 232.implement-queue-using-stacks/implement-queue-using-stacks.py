from collections import deque


class Queue(object):
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack1 = deque([])
    self.stack2 = deque([])

  def push(self, x):
    """
    :type x: int
    :rtype: nothing
    """
    self.stack1.append(x)

  def pop(self):
    """
    :rtype: nothing
    """
    self.peek()
    self.stack2.pop()

  def peek(self):
    """
    :rtype: int
    """
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
      return self.stack2[-1]
    else:
      return self.stack2[-1]

  def empty(self):
    """
    :rtype: bool
    """
    return not self.stack1 and not self.stack2
