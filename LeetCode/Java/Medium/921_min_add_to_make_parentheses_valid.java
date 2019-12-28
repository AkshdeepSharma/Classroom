class Solution {
    public int minAddToMakeValid(String S) {
        Stack<Character> stack = new Stack<>();
        int count = 0;
        for (char paren : S.toCharArray()){
            if(paren == '(')
                stack.push('(');
            else if(paren == ')' && stack.size() != 0)
                stack.pop();
            else
                count++;
        }
        return count + stack.size();
    }
}