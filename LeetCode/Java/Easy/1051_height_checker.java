class Solution {
    public int heightChecker(int[] heights) {
        int[] sortedHeights = heights.clone();
        int count = 0;
        Arrays.sort(sortedHeights);
        for(int i = 0; i < heights.length; i++)
            if(sortedHeights[i] != heights[i])
                count++;
        return count;
    }
}