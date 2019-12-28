class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> ans = new ArrayList<>();
        for (int i = left; i <= right; i++)
            if (isValid(i))
                ans.add(i);
        return ans;
    }
    
    public boolean isValid(int num) {
        int curr = num;
        while(curr != 0){
            int digit = curr % 10;
            if (digit == 0 || num % digit != 0)
                return false;
            curr /= 10;
        }
        return true;
    }
}