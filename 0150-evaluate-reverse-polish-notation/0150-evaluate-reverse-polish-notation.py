class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = set("+-*/")
        stack = []
        p = 0

        while p < len(tokens):
            stack.append(tokens[p])
            p += 1

            if stack and stack[-1] in op:
                o, b, a = stack.pop(), int(stack.pop()), int(stack.pop())
                if o == "+":
                    stack.append(a+b)
                elif o == "/":
                    stack.append(a/b)
                elif o == "*":
                    stack.append(a*b)
                else:
                    stack.append(a-b)
        
        return int(stack[0])
        