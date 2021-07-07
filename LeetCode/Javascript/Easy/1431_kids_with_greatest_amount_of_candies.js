const kidsWithCandies = (candies, extraCandies) => {
    const maxCandies = Math.max(...candies);
    let ans = [];
    for(let i=0; i < candies.length; i++){
        if(candies[i] + extraCandies >= maxCandies)
            ans.push(true);
        else
            ans.push(false);
    };
    return ans;
};