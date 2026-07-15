class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> set = new HashSet<>();
        for (String word : words) {
            set.add(word);
        }

        for (String word : words) {
            if (!set.contains(word)) continue;
            for (int i = 1; i < word.length(); i++) {
                set.remove(word.substring(i));
            }
        }

        int res = 0;
        for (String word : set) {
            res += word.length() + 1;
        }

        return res;
    }
}