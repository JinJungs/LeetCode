from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n-1

        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]
            if s > target:
                end -= 1
            else:
                start += 1