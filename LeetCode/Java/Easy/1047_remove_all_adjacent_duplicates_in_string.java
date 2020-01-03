class Solution {
    public String removeDuplicates(String S) {
        Stack<Character> stack = new Stack<Character>();
        for(char c : S.toCharArray()){
            if(stack.empty() || stack.peek() != c)
                stack.push(c);
            else if(stack.peek() == c)
                stack.pop();
        }
        StringBuilder ans = new StringBuilder();
        for(char c : stack)
            ans.append(c);
        return ans.toString();
    }
}