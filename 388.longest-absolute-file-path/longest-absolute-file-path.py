class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxLen = 0
        curLen = 0
        stack = []
        dfa = {"init": 0, "char": 1, "escapeCMD": 2, "file": 3}
        state = 0
        start = 0
        level = 0
        
        for i in xrange(0, len(input)):
            chr = input[i]
            if chr == '\n':
                curLen = 0 if len(stack) == 0 else stack[-1][1]
                if state == dfa["char"]:
                    curLen += i - start
                    stack.append((input[start:i], curLen + 1, level))
                elif state == dfa["file"]:
                    maxLen = max(maxLen, curLen + (i - start))
                else:
                    return -1
                state = dfa["escapeCMD"]
                level = 0
            elif chr == '\t':
                if state == dfa["escapeCMD"]:
                    level += 1
                else:
                    return "TAB cannot be here"
            elif chr == '.':
                if state == dfa["char"] or state == dfa["file"] or state == dfa["escapeCMD"]:
                    state = dfa["file"]
                else:
                    return "unexpected char before dot", state
            else:
                if state == dfa["escapeCMD"]:
                    while stack and stack[-1][2] >= level:
                        stack.pop()
                    start = i
                    state = dfa["char"]
                elif state == dfa["init"]:
                    state = dfa["char"]
                elif i == len(input) - 1:
                    curLen = 0 if len(stack) == 0 else stack[-1][1]
                    maxLen = max(maxLen, curLen + (i - start) + 1)

            # print 'state:', state
            # print 'stack:', stack
            # print 'level', level 
        return maxLen
                    