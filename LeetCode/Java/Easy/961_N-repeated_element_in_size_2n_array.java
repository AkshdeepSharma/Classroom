class Solution {
    public int repeatedNTimes(int[] A) {
        HashSet<Integer> num_map = new HashSet<Integer>();
        for(int num : A){
            if(!num_map.add(num))
                return num;
        }
        return -1;
    }
}