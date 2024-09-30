class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # direction
        def indexAndDirection(index: int, d: str):
            if d == 'U' and index == 0:
                d = 'D'
            if d == 'D' and index == numRows - 1:
                d = 'U'

            if d == 'U':
                index -= 1
            else:
                index += 1

            return index, d

        result = ['' for _ in range(numRows)]
        index = 0
        d = 'D'
        for c in s:
            result[index] += c
            index, d = indexAndDirection(index, d)

        return ''.join(result)


