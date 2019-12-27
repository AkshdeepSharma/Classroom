class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        for (int i = 0; i < S.length(); i++) {
            if (J.contains(Character.toString(S.charAt(i))))
                count += 1;
        }
        return count;
    }
}