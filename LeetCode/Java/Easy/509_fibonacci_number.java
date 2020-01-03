class Solution {
    public int fib(int N) {
        int a = 0, b = 1, temp = 0;
        if(N == 0)
            return 0;
        for(int i = 1; i < N; i++){
            temp = a;
            a = b;
            b += temp;
        }
        return b;
    }
}