class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = 0
        output = ''
        ra = ''.join(reversed(a))
        rb = ''.join(reversed(b))

        for i in range(max(len(a), len(b))):
            if i > len(a) -1:
                total = int(rb[i]) + add
            elif i > len(b) -1:
                total = int(ra[i]) + add
            else:
                total = int(ra[i]) + int(rb[i]) + add

            remain = total % 2
            add = total // 2
            output = str(remain) + output

        return output if add == 0 else str(add)+output