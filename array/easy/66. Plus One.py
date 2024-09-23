from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1, -1, -1):
            added = digits[i] + add
            add = added // 10
            digits[i] = added % 10

        if add != 0:
            result = [add]
            for digit in digits:
                result.append(digit)
            return result

        return digits