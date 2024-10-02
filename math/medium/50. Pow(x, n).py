class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        m = abs(n)
        result = 1.0
        current = x

        while m > 0:
            if m % 2 == 1:
                result *= current
            current *= current
            m //= 2

        return result if n > 0 else 1/result

