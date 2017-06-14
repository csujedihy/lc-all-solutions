class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            stack = []
            for c in s:
                if c == "(":
                    stack.append("(")    
                elif c == ")":
                    stack.append(")")
                    if len(stack) >= 2 and stack[-2] + stack[-1] == "()":
                        stack.pop()
                        stack.pop()
            return len(stack)
   
        def dfs(s, res, cache, length):
            if s in cache:
                return

            if len(s) == length:
                if isValid(s) == 0:
                    res.append(s)
                    return
            
            for i in xrange(0, len(s)):
                if s[i] == "(" or s[i] == ")" and len(s) - 1 >= length:
                    dfs(s[:i] + s[i + 1:], res, cache, length)
                    cache.add(s[:i] + s[i + 1:])

        prepLeft = ""
        for i in xrange(0, len(s)):
            if s[i] == "(":
                prepLeft += s[i:]
                break
            elif s[i] != ")":
                prepLeft += s[i]
                
        prepRight = ""
        for i in reversed(xrange(0, len(prepLeft))):
            if prepLeft[i] == ")":
                prepRight += prepLeft[:i + 1][::-1]
                break
            elif prepLeft[i] != "(":
                prepRight += prepLeft[i]
                
        s = prepRight[::-1]
        length = len(s) - isValid(s)
        res = []
        cache = set()
        dfs(s, res, cache, length)
        return res