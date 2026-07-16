class Solution {
    Set<Character> vowels = new HashSet<>(Set.of('a','e','i','o','u'));

    public int[] vowelStrings(String[] words, int[][] queries) {
        int n = words.length;
        int[] prefix = new int[n+1];

        for (int i = 0; i < n; i++) {
            prefix[i+1] = prefix[i] + (isVowelString(words[i]) ? 1 : 0);
        }

        int m = queries.length;
        int[] res = new int[m];
        for (int i = 0; i < m; i++) {
            int start = queries[i][0];
            int end = queries[i][1];
            res[i] = prefix[end+1] - prefix[start];
        }

        return res;
    }

    private boolean isVowelString(String word) {
        return vowels.contains(word.charAt(0)) && vowels.contains(word.charAt(word.length() - 1));
    }
}