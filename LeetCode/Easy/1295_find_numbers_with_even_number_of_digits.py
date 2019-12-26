class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

'''Java
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            String number = Integer.toString(nums[i]);
            if (number.length() % 2 == 0)
                count += 1;
        }
        return count;
    }
}
'''