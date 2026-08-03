class Solution {
    public int numSteps(String s) {
        if ("1".equals(s)) {
            return 0;
        }

        int n = s.length();
        int carry = 0;
        int res = 0;

        for (int i = n-1; i > 0; i--) {
            int curr = s.charAt(i) - '0' + carry;
            if (curr == 1) {
                carry = 1;
                res++;
            } else if (curr == 2) {
                carry = 1;
            }
            res++;
        }
        
        return res + carry;
    }
}
