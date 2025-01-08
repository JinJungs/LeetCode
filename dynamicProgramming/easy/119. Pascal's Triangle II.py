from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        1
        1 1
        1 2 1
        1 3 3 1
        1 4 6 4 1
        """
        prev = [1]
        for i in range(1, rowIndex+1):
            curr = [1]

            for j in range(1, i):
                curr.append(prev[j-1] + prev[j])

            curr.append(1)
            prev = curr

        return prev
