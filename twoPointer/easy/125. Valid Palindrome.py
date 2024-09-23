class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [i for i in s if i.isalpha() or i.isnumeric()]
        ns = ''.join(s_list)
        lower_s = ns.lower()

        if not lower_s or len(lower_s) == 0:
            return True

        q = len(lower_s) // 2
        r = len(lower_s) % 2

        # even
        if r == 0:
            left = lower_s[0:q]
            right = ''.join(reversed(lower_s[q:]))
            return left == right
        else:
            left = lower_s[0:q]
            right = ''.join(reversed(lower_s[q+1:]))
            return left == right
