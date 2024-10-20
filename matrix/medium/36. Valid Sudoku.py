from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            l = []
            for num in row:
                if num == '.':
                    continue
                if num in l:
                    return False
                l.append(num)

        # column
        m = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                if j not in m.keys():
                    m[j] = [num]
                    continue
                if num in m[j]:
                    return False
                m[j].append(num)

        # 3 * 3 grid
        b = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                key1 = i // 3
                key2 = j // 3
                if key1 not in b.keys():
                    b[key1] = {key2: [num]}
                    continue
                if key2 not in b[key1].keys():
                    b[key1][key2] = [num]
                    continue
                if num in b[key1][key2]:
                    return False
                b[key1][key2].append(num)

        return True