import sys

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        # On
        for i in range(sys.maxsize):
            if i*i <= x < (i+1)*(i+1):
                return i
        '''

        # binary search
        def binary(x: int, s: int, e: int):
            if e - s <= 1:
                return s
            m = (s+e) // 2
            if s*s <= x < m*m:
                return binary(x, s, m)
            else:
                return binary(x, m, e)

        return binary(x, 0, sys.maxsize)

