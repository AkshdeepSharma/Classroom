var numJewelsInStones = function(jewels, stones) {
    let ans = 0;
    const setJewels = new Set(jewels);
    for (let i=0; i < stones.length; i++) {
        if (setJewels.has(stones[i])){
            ans++;
        }
    }
    return ans;
};