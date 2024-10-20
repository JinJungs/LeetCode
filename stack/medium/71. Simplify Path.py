class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        s = []
        for p in path_list:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if len(s) == 0:
                    continue
                else:
                    s.pop()
            else:
                s.append(p)

        return '/' + '/'.join(s)