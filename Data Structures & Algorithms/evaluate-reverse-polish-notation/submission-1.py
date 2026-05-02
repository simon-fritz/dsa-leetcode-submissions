class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        stack = []
        while tokens:
            x = tokens.pop()
            if x in "+-*/":
                n2 = stack.pop()
                n1 = stack.pop()
                if x == "+":
                    n1 = n1 + n2
                elif x == "-":
                    n1 = n1 - n2
                elif x == "*":
                    n1 = n1 * n2
                else:
                    n1 = int(n1 / n2)
                stack.append(n1)
            else:
                stack.append(int(x))
        return stack[0]