class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    record = {}
    sq_sum = 0
    while n != 1:
      sq_sum = 0
      sub_num = n
      while sub_num > 0:
        sq_sum += (sub_num % 10) * (sub_num % 10)
        sub_num /= 10
      if sq_sum in record:
        return False
      else:
        record[sq_sum] = 1
      n = sq_sum
    return True
