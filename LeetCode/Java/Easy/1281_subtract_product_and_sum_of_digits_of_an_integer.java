class Solution {
    public int subtractProductAndSum(int n) {
        String nString = Integer.toString(n);
        int sum = 0;
        int product = 1;
        for (int i = 0; i < nString.length(); i++){
            int num = Character.getNumericValue(nString.charAt(i));
            sum += num;
            product *= num;
        }
        return product - sum;
    }
}