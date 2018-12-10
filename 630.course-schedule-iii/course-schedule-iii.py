# idea:
# sort all courses by deadline
# iterate all sorted courses
# if current course is able to be taken, then take it
# if not, check if we can remove some courses from courses we already taken
# if the one has the maximal duration is greater than current course's duration
# then replace it by current course
# since courses are already sorted by deadline, then our new deadline must be later
# (why? because sorted by deadline, current deadline must be later than all deadlines of taken courses, 
# so it must be valid)
# moreover, we have more available time for taking more courses

class Solution(object):
  def scheduleCourse(self, courses):
    """
    :type courses: List[List[int]]
    :rtype: int
    """
    now = 0
    heap = []
    for t, d in sorted(courses, key=lambda x: x[1]):
      if now + t <= d:
        now += t
        heapq.heappush(heap, -t)
      elif heap and -heap[0] > t:
        now += t + heapq.heappop(heap)
        heapq.heappush(heap, -t)
    return len(heap)
