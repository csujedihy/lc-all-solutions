import heapq
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        leftBound = rectangles[0][0]
        rightBound = rectangles[0][2]
        bottomBound = rectangles[0][1]
        topBound = rectangles[0][3]
        lines = []
        realArea = 0
        for rect in rectangles:
            leftBound = min(leftBound, rect[0])
            rightBound = max(rightBound, rect[2])
            bottomBound = min(bottomBound, rect[1])
            topBound = max(topBound, rect[3])
            realArea += (rect[3] - rect[1]) * (rect[2] - rect[0])
            lines.append((rect[0], 1, rect[1], rect[3]))
            lines.append((rect[2], -1, rect[1], rect[3]))
        area = (rightBound - leftBound) * (topBound - bottomBound)
        if area != realArea:
            return False
        lines.sort()
        bst = []
        for line in lines:
            x, flag, bottom, top = line
            if flag > 0:
                idx = bisect.bisect_right(bst, (bottom, top))
                bisect.insort_right(bst, (bottom, top))
                if idx + 1 < len(bst) and bst[idx + 1][0] < bst[idx][1] or idx > 0 and bst[idx][0] < bst[idx - 1][1]:
                    return False
            else:
                bst.remove((bottom, top))
        return area == realArea