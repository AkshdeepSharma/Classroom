class Solution {
    public int numTilePossibilities(String tiles) {
        int[] alphabet = new int[26];
        for (char c : tiles.toCharArray())
            alphabet[c - 'A']++;
        return dfs(alphabet);
    }
    
    int dfs(int[] arr) {
        int sum = 0;
        for (int i=0; i < 26; i++){
            if(arr[i] == 0)
                continue;
            sum++;
            arr[i]--;
            sum += dfs(arr);
            arr[i]++;
        }
        return sum;
    }
}