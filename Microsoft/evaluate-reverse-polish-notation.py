class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+" : add, "-" : sub, "*" : mul, "/" : truediv}
        for i in tokens:
            if i in ops:
                b, a = stack.pop(),stack.pop()
                i = ops[i](a,b)
            stack.append(int(i))
        return stack[-1] 