class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        num = n
        memo = dict()
        while True:
            num = sum([int(x) * int(x) for x in list(str(num))])
            if num == 1:
                return True
            elif num in memo.keys():
                return False
            memo[num] = num
