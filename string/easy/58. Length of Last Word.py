class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = s.rstrip()
        result = 0
        for i in range(len(sl)-1, -1, -1):
            if sl[i] == ' ':
                break
            result += 1
        return result