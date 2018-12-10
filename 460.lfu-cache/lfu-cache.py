class List(object):
  @staticmethod
  def delete(elem):
    elem.prev.next = elem.next
    elem.next.prev = elem.prev
    elem.next = elem.prev = None
    return elem

  @staticmethod
  def move(elem, newPrev, newNext):
    elem.prev = newPrev
    elem.next = newNext
    newPrev.next = elem
    newNext.prev = elem

  @staticmethod
  def append(head, elem):
    List.move(elem, head.prev, head)

  @staticmethod
  def insertAfter(head, elem):
    List.move(elem, head, head.next)

  @staticmethod
  def isEmpty(head):
    return head.next == head.prev == head

  @staticmethod
  def initHead(head):
    head.prev = head.next = head


class FreqNode(object):
  def __init__(self, freq):
    self.prev = self.next = None
    self.freq = freq
    self.head = Cache(-1, -1, self)
    List.initHead(self.head)

  def popCache(self):
    head = self.head
    ret = List.delete(head.next)
    if List.isEmpty(head):
      List.delete(self)
    return ret


class Cache(object):
  def __init__(self, key, val, freqNode):
    self.prev = self.next = None
    self.freqNode = freqNode
    self.val = val
    self.key = key

  def increaseFreq(self):
    freqNode = self.freqNode
    newFreqNode = None
    if List.isEmpty(freqNode) or freqNode.next.freq != freqNode.freq + 1:
      newFreqNode = FreqNode(self.freqNode.freq + 1)
      List.insertAfter(freqNode, newFreqNode)
    else:
      newFreqNode = freqNode.next
    self.freqNode = newFreqNode
    List.delete(self)
    List.append(newFreqNode.head, self)
    if List.isEmpty(freqNode.head):
      List.delete(freqNode)


class LFUCache(object):
  def __init__(self, capacity):
    self.d = {}
    self.cap = capacity
    self.head = FreqNode(-1)
    List.initHead(self.head)

  def get(self, key):
    if key not in self.d:
      return -1
    cacheNode = self.d[key]
    cacheNode.increaseFreq()
    return cacheNode.val

  def set(self, key, value):
    if self.cap == 0:
      return
    if key in self.d:
      cacheNode = self.d[key]
      cacheNode.val = value
      cacheNode.increaseFreq()
    else:
      if len(self.d) >= self.cap:
        del self.d[self.head.next.popCache().key]
      newFreqNode = FreqNode(0)
      newCacheNode = Cache(key, value, newFreqNode)
      List.append(newFreqNode.head, newCacheNode)
      List.insertAfter(self.head, newFreqNode)
      self.d[key] = newCacheNode
      newCacheNode.increaseFreq()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
