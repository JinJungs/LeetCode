class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(' ')
        if len(l) != len(pattern):
            return False

        d1 = dict()
        d2 = dict()

        for i in range(len(pattern)):
            p = pattern[i]
            if p in d1.keys() and d1[p] != l[i]:
                return False
            if l[i] in d2.keys() and d2[l[i]] != p:
                return False
            d1[p] = l[i]
            d2[l[i]] = p

        return True