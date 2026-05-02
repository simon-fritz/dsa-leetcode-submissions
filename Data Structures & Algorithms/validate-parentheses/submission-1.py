class Solution:
    def isValid(self, s: str) -> bool:
        openings = "([{"
        closings = ")]}"
        stack = []
        for l in s:
            if l in openings:
                stack.append(l)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if not c:
                    return False
                if c == "{" and l != "}":
                    return False
                if c == "(" and l != ")":
                    return False
                if c == "[" and l != "]":
                    return False
        if stack:
            return False
        return True
        