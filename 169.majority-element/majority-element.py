class Solution(object):
  def majorityElement(self, num):
    return sorted(num)[len(num) / 2]
