class Solution {
    public String removeOuterParentheses(String S) {
        StringBuilder ans = new StringBuilder();
        int open = 0, close = 0, start = 0;
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '(')
                open++;
            else
                close++;
            if(open == close){
                ans.append(S.substring(start + 1, i));
                start = i + 1;
            }
        }
        return ans.toString();
    }
}