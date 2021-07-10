const numIdenticalPairs = nums => {
    const counts = {};
    let ans = 0;
    for(let i=0; i < nums.length; i++){
        if(nums[i] in counts)
            counts[nums[i]]++;
        else
            counts[nums[i]] = 1;
    }
    for (let [key, value] of Object.entries(counts)) {
        ans += value * (value - 1) / 2;
    }
    return ans;
};