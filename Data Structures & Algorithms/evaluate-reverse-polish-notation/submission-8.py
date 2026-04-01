class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = {"+", "-", "*", "/"}
        if len(tokens) == 1:
            return int(tokens[0])
        opstack = [int(tokens[0]), int(tokens[1])]
        for i in range(2, len(tokens)):
            key = tokens[i]
            if key not in ops:
                opstack.append(int(key))
            else:
                if key == "+":
                    res = opstack[len(opstack) - 2] + opstack[-1]
                    opstack.pop()
                    opstack.pop()
                    opstack.append(res)
                elif key == "-":
                    res = opstack[len(opstack) - 2] - opstack[-1]
                    opstack.pop()
                    opstack.pop()
                    opstack.append(res)
                elif key == "*":
                    res = opstack[len(opstack) - 2] * opstack[-1]
                    opstack.pop()
                    opstack.pop()
                    opstack.append(res)
                elif key == "/":
                    cond = opstack[len(opstack) - 2] / opstack[-1]
                    if cond > 0:
                        res = opstack[len(opstack) - 2] // opstack[-1]
                    elif cond == 0:
                        res = 0
                    elif cond < 0 and opstack[len(opstack) - 2] % opstack[-1] == 0:
                        res = opstack[len(opstack) - 2] // opstack[-1]
                    else:
                        res = opstack[len(opstack) - 2] // opstack[-1] + 1
                    opstack.pop()
                    opstack.pop()
                    opstack.append(res)           
        return opstack[0]
        


