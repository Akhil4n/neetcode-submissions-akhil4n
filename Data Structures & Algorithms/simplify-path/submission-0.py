class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0
        while i < len(path):
            char = path[i]
            curr = []
            while i < len(path) and path[i] == '/':
                i += 1
            while i < len(path) and path[i] != '/':
                curr.append(path[i])
                i += 1
            print(i, curr)
            add = "".join(curr)
            if len(add) == 0:
                continue
            if add == '.':
                continue
            elif add == '..':
                if res:
                    res.pop()
            else:
                res.append(add)
            print(res)
        return "/" + "/".join(res)











        