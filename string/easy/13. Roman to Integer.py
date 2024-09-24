class Solution:
    def romanToInt(self, s: str) -> int:
        def roman(d: str) -> int:
            if d == 'I':
                return 1
            if d == 'V':
                return 5
            if d == 'X':
                return 10
            if d == 'L':
                return 50
            if d == 'C':
                return 100
            if d == 'D':
                return 500
            if d == 'M':
                return 1000
            return 0

        def minusValue(before: str, after: str) -> int:
            if before == 'I' and after in ('V', 'X'):
                return 2
            if before == 'X' and after in ('L', 'C'):
                return 20
            if before == 'C' and after in ('D', 'M'):
                return 200
            return 0

        result = 0
        for i in range(len(s)):
            if i !=0:
                result -= minusValue(s[i-1], s[i])
            result += roman(s[i])

        return result
