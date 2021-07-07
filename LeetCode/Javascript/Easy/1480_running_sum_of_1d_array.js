var runningSum = function(nums) {
    let ans = [];
    let runningSum = 0;
    for(let i=0; i < nums.length; i++){
        runningSum += nums[i]
        ans.push(runningSum);
    }
    return ans;
};